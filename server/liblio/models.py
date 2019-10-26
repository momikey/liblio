from flask import json, current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from enum import Enum
import re

from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSONB

from liblio.helpers import flake_id, printable_id

# Create the DB object, so we can build models from it.
# (Note that we set it up in the main app.)
db = SQLAlchemy()

### Helpers ###

def render_content(context):
    """Create the rendered form of this post's content."""

    content_type = context.get_current_parameters()['content_type']
    source = context.get_current_parameters()['source']

    if content_type == 'text/html':
        return source
    else:
        raise ValueError("Can't convert from source type {type}".format(type=content_type))

def create_uri(context, path_prefix):
    """Create a URI for any local data with a Flake ID."""

    flake = context.get_current_parameters()['flake']
    origin = current_app.config['SERVER_ORIGIN']
    scheme = 'https' if current_app.config['HTTPS_ENABLED'] else 'http'

    path = "{prefix}/{id}".format(prefix=path_prefix, id=printable_id(flake))

    return "{scheme}://{origin}/{path}".format(scheme=scheme, origin=origin, path=path)

def create_post_uri(context):
    """Create a URI for a local post."""

    path_prefix = "post"

    return create_uri(context, path_prefix)

def create_avatar_uri(context):
    """Create a URI for a user's avatar."""

    path_prefix = current_app.config["AVATARS_URI_DIR"]

    return create_uri(context, path_prefix)

def create_upload_uri(context):
    """Create a URI for a media upload."""

    path_prefix = current_app.config["MEDIA_URI_DIR"]

    return create_uri(context, path_prefix)

def create_tag_uri(name):
    """Create a local URI for a tag."""

    origin = current_app.config['SERVER_ORIGIN']
    scheme = 'https' if current_app.config['HTTPS_ENABLED'] else 'http'

    path = "tag/{name}".format(name=name)

    return "{scheme}://{origin}/{path}".format(scheme=scheme, origin=origin, path=path)

# UTC timestamp handling
# TODO: Other databases, if we want to support them
class utcnow(expression.FunctionElement):
    """UTC timestamp expression class, as per SQLAlchemy docs"""
    type = TIMESTAMP()

@compiles(utcnow, 'postgresql')
def utcnow_pg(element, compiler, **kwargs):
    """UTC timestamps for Postgres"""
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"

### Roles ###

class Role(Enum):
    banned = 0
    admin = 1
    user = 2

### Association Tables ###

# Likes connect users (`likes` property) to posts (`liking` property)
likes = db.Table('likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)

# Shares (aka boosts, reposts, announces) connect users' `sharing` property
# to posts `shares` property.
shares = db.Table('shares',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)

# Follows connect users (`following` property) to other users (`followers` property)
# This is a self-referential many-to-many relation, probably one of the most
# convoluted kind there is.
follows = db.Table('follows',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

# User/post tags connect either users or posts to tags
user_tags = db.Table('user_tags',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

### Models ###

class Login(db.Model):
    """A login is just the basic authentication for a Liblio user."""

    __tablename__ = "logins"

    id = db.Column(db.Integer, primary_key=True)
    
    # The username
    username = db.Column(db.String(64), unique=True, nullable=False)

    # The (hashed!) password for this user
    password = db.Column(db.Text, nullable=False)

    # The eamil address associated with this login
    # Note: We make this unique to facilitate lookups, password resets, etc.
    email = db.Column(db.Text, unique=True, nullable=False)

    # Last login time
    # We keep this for stats purposes, nothing more.
    last_login = db.Column(db.DateTime, nullable=True)

    # Last "action" time
    # Basically, this is the last time this user accessed a protected API.
    # We keep it for activity stats.
    last_action = db.Column(db.DateTime, nullable=True)

    # Relation to the user profile for this account
    user = db.relationship('User', back_populates='login')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # User role (admin, regular user, etc.)
    role = db.Column(db.Enum(Role), server_default="user")

    def __repr__(self):
        return "<Login {self.username} ({self.role.name} / {self.email}>".format(self=self)

    def set_password(self, pw):
        """Hash a user's password to securely store in the database."""
        self.password = generate_password_hash(pw)

    def check_password(self, pw):
        """Check that a given password hashes to the known value, and is thus correct."""
        return check_password_hash(self.password, pw)

class User(db.Model):
    """A user is any Liblio user, whether from this server or another."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    # The relation to this user's login credentials
    # This is only valid for users on this server. It is normally only
    # accessed from the login side, but that is much more difficult to model.
    # SQL note: This is a one-to-one relation.
    login = db.relationship('Login', uselist=False, back_populates='user')

    # The relation to this user's posts
    posts = db.relationship('Post', back_populates='user')

    # The username
    # Note: this is a duplicate field for local users, but not for those from
    # other servers, so we can't necessarily connect it to a login.
    username = db.Column(db.String(64), nullable=False)

    # The originating server
    origin = db.Column(db.String, nullable=False)

    # The user's "display" name; i.e., how the user wishes to be seen
    # (This can be left blank, in which case the username will be used instead.)
    display_name = db.Column(db.String, nullable=True)

    # The user's bio (or description, or whatever you wish to call it)
    # This is a more freeform text field, and it can be any length, though clients
    # and some servers may restrict it.
    bio = db.Column(db.Text, nullable=True)

    # Whether this profile is "private" (i.e., doesn't show up in listings)
    # Note that a private profile may still be accessibly to followers, etc.
    private = db.Column(db.Boolean, nullable=False, default=False, server_default='false')

    # This user's liked posts
    likes = db.relationship('Post', secondary=likes, back_populates='liking')

    # This user's shared posts
    sharing = db.relationship('Post', secondary=shares, back_populates='shares')

    # This user's uploaded media
    uploads = db.relationship('Upload', back_populates='user')

    # All of this user's avatars
    avatars = db.relationship('Avatar', back_populates='user')

    # This user's current avatar
    # Note: This is intentionally a one-way relationship. Avatars don't care
    # if they're currently in use. Also, it's one-to-one, because a user can
    # only have one current avatar.
    current_avatar = db.relationship('Avatar', uselist=False)

    # This user' followers/followed users
    followers = db.relationship('User',
        secondary=follows,
        primaryjoin='User.id == follows.c.followed_id',
        secondaryjoin='User.id == follows.c.follower_id',
        backref='following'
    )

    # This user's profile tags
    tags = db.relationship('Tag', secondary=user_tags, back_populates='users')

    def __repr__(self):
        return '<User "{self.display_name}" ({self.username}@{self.origin})>'.format(self=self)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            origin=self.origin,
            display_name=self.display_name,
            bio=self.bio,
            private=self.private,
            followers=[f.id for f in self.followers],
            following=[f.id for f in self.following],
            tags=[t.name for t in self.tags],
            avatar=self.current_avatar
        )

class Post(db.Model):
    """A post on a Liblio server, including posts received via federation from other servers."""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)

    # The relationship to this post's owner
    # Note that we're using `back_populates` to make things more obvious.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='posts')

    # The post's subject (optional)
    # In some ActivityPub servers, this may render as a content warning.
    subject = db.Column(db.String, nullable=True)

    # The post's source content
    # We will eventually support Markdown (and possibly BBCode), but we have to store
    # the original post source for clients that can't understand HTML.
    source = db.Column(db.Text, nullable=False)

    # The post's content type
    # TODO: We may need to make this an enum or something.
    content_type = db.Column(db.String, default='text/html')

    # The "cooked" form of the post
    # In the case of posts constructed in, e.g., Markdown, this will be a rendered form
    # of the `source` property.
    content = db.Column(db.Text, nullable=False, default=render_content)

    # The post's Flake ID
    # This is different from the database ID, and we'll use it in URIs, but only
    # after we convert it to something printable.
    flake = db.Column(db.BigInteger, nullable=False, default=flake_id)

    # This post's URI
    # For local posts, we will generate this. For foreign posts, it will come as
    # the "id" property of the ActivityPub object.
    uri = db.Column(db.String, nullable=False, default=create_post_uri)

    # This post's timestamp
    # For local posts, this will be generated; foreign posts will provide it.
    timestamp = db.Column(TIMESTAMP, nullable=False, server_default=utcnow())

    # The post's parent and/or children
    # This uses a self-referential foreign key. If that's NULL, then this is
    # a top-level post. Otherwise, it's a reply to another post.
    parent_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=True)
    children = db.relationship('Post', backref=db.backref('parent', remote_side=[id]))

    # All users who like this post
    liking = db.relationship('User', secondary=likes, back_populates='likes')

    # All users who have shared this post
    shares = db.relationship('User', secondary=shares, back_populates='sharing')

    # Any tags given to this post
    tags = db.relationship('Tag', secondary=post_tags, back_populates='posts')

    # Any uploads attached to this post
    uploads = db.relationship('Upload', back_populates='post')

    # Arbitrary metadata that may be attached to a post
    # (Note that SQLAlchemy won't let us give this a proper name.
    # There is no valid reason for this.)
    post_meta = db.Column(MutableDict.as_mutable(JSONB))

    def __repr__(self):
        return '<Post "{subject}" by {user}@{origin}>'.format(
            subject=self.short_subject(),
            user=self.user.username,
            origin=self.user.origin
        )

    def short_subject(self, length=16):
        """Shorten this post's subject to fit in a given length, if necessary."""

        if self.subject is None or len(self.subject) == 0:
            return '(no subject)'
        elif len(self.subject) > length:
            return self.subject[:length] + '...'
        else:
            return self.subject

    def to_dict(self):
        return dict(
            id=self.id,
            user=self.user.to_dict() if self.user is not None else None,
            subject=self.subject,
            source=self.source,
            content_type=self.content_type,
            content=self.content,
            flake=self.flake,
            uri=self.uri,
            parent_id=self.parent_id,
            timestamp=self.timestamp,
            tags=[t.to_dict() for t in self.tags],
            files=[{'uri': file.uri, 'type': file.mimetype} for file in self.uploads],
            metadata=self.post_meta if self.post_meta is not None else {}
        )

class Tag(db.Model):
    """A tag for a post or user on a Liblio server."""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)

    # Tags really have only two properties: a name and a description.
    # If a tag is picked up in a post from a non-Liblio server, it will
    # have no description initially, but an admin should be allowed to
    # add one if necessary.
    name = db.Column(db.String, nullable=False)

    description = db.Column(db.String, nullable=True)

    # Relation properties
    users = db.relationship('User', secondary='user_tags', back_populates='tags')
    posts = db.relationship('Post', secondary='post_tags', back_populates='tags')

    def __repr__(self):
        return "<Tag {self.name}>".format(self=self)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description
        )

    def uri(self):
        return create_tag_uri(self.name)

    @staticmethod
    def normalize_name(name):
        """Normalize the name of a tag, removing spaces and punctuation."""
        return re.sub(r'\W', '', name).casefold()

class Upload(db.Model):
    """Any uploaded media."""

    __tablename__ = 'uploads'

    id = db.Column(db.Integer, primary_key=True)

    # The Flake ID for this upload
    # We store this to generate filenames and URIs.
    flake = db.Column(db.BigInteger, nullable=False, default=flake_id)

    # The filename for this upload
    # This is relative to the uploads directory (UPLOADS_DEFAULT_DEST)
    filename = db.Column(db.String, nullable=False)

    # The original URI for this upload
    uri = db.Column(db.String, nullable=False, default=create_upload_uri)

    # The uploaded media's MIME type
    # The front end can use this to determine how to display it (e.g., images
    # will be in an <img> tag, audio/video with a player)
    mimetype = db.Column(db.String, nullable=False, server_default="application/octet-stream")
    
    # The user who uploaded this media
    user = db.relationship('User', back_populates='uploads')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # The post the upload is attached to
    post = db.relationship('Post', back_populates='uploads')
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

class Avatar(db.Model):
    """A user's avatar."""

    __tablename__ = 'avatars'

    id = db.Column(db.Integer, primary_key=True)

    # This avatar's Flake ID
    # We keep these to generate filenames in cases where they aren't
    # provided by the user.
    flake = db.Column(db.BigInteger, nullable=False, default=flake_id)

    # The URI for this avatar
    # Note: This can be either local or foreign, and we'll use it when
    # making ActivityPub objects, actors, etc.
    uri = db.Column(db.String, nullable=False, default=create_avatar_uri)

    # The local filename for this avatar
    # This is relative to the uploads directory (UPLOADS_DEFAULT_DEST)
    filename = db.Column(db.String, nullable=False)

    # The user who uploaded this avatar
    user = db.relationship('User', back_populates="avatars")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # A timestamp for when the user uploaded the avatar or,
    # in the case of foreign users, when we last downloaded it.
    timestamp = db.Column(TIMESTAMP, nullable=False, server_default=utcnow())

class Configuration(db.Model):
    """Server configuration. This is only those parts which can be changed
    while the server is running. Settings such as ports and directories must
    be configured before starting the server."""

    id = db.Column(db.Integer, primary_key=True)

    # Server settings are stored as a JSON object, since keys are all strings,
    # but data can be strings, numbers, or booleans.
    # TODO: Check if the server isn't running Postgres, because the JSONB type
    # we're using is specific to that DB.
    # TODO: Do we need multiple objects? Possibly for different sets of settings?
    data = db.Column(MutableDict.as_mutable(JSONB))

    @classmethod
    def data_object(cls, db):
        """Return the data object for the first defined configuration. At this time
        that will be the only configuration."""
        d = cls.query.first()

        # If there isn't a data object already in the DB, create one and add it.
        if d is None:
            d = cls(data={})
            db.session.add(d)
            db.session.commit()
        
        return d;