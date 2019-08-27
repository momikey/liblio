from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# Create the DB object, so we can build models from it.
# (Note that we set it up in the main app.)
db = SQLAlchemy()

### Models ###

class Login(db.Model):
    """A login is just the basic authentication for a Liblio user"""

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

    def __repr__(self):
        return "<Login {self.username} / {self.email}>".format(self=self)

    def set_password(self, pw):
        """Hash a user's password to securely store in the database."""
        self.password = generate_password_hash(pw)

    def check_password(self, pw):
        """Check that a given password hashes to the known value, and is thus correct."""
        return check_password_hash(self.password, pw)
