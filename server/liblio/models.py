from flask import json, current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

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

def create_uri(context):
    """Create a URI for a local post."""

    flake = context.get_current_parameters()['flake']
    origin = current_app.config['SERVER_ORIGIN']
    scheme = 'https' if current_app.config['HTTPS_ENABLED'] else 'http'

    path = "post/{id}".format(id=printable_id(flake))

    return "{scheme}://{origin}/{path}".format(scheme=scheme, origin=origin, path=path)

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

    def __repr__(self):
        return "<Login {self.username} / {self.email}>".format(self=self)

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

    # TODO: Roles and tags (these have to be relations, so they can wait until
    # we actually have the models done)

    def __repr__(self):
        return '<User "{self.display_name}" ({self.username}@{self.origin})>'.format(self=self)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            origin=self.origin,
            display_name=self.display_name,
            bio=self.bio,
            private=self.private
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
    uri = db.Column(db.String, nullable=False, default=create_uri)

    # This post's timestamp
    # For local posts, this will be generated; foreign posts will provide it.
    timestamp = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

    # The post's parent and/or children
    # This uses a self-referential foreign key. If that's NULL, then this is
    # a top-level post. Otherwise, it's a reply to another post.
    parent_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=True)
    children = db.relationship('Post', backref=db.backref('parent', remote_side=[id]))

    def __repr__(self):
        return '<Post "{subject}" by {user}@{origin}>'.format(
            subject=self.short_subject(),
            user=self.user.username,
            origin=self.user.origin
        )

    def short_subject(self, length=16):
        """Shorten this post's subject to fit in a given length, if necessary."""

        if len(self.subject) > length:
            return self.subject[:length] + '...'
        elif self.subject is None or len(self.subject) == 0:
            return '(no subject)'
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
            timestamp=self.timestamp
        )