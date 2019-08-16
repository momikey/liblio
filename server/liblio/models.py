from flask_sqlalchemy import SQLAlchemy

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
    # TODO: Do we make this unique? Pros: better security/moderation; Cons: can lose accounts
    email = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return "<Login {self.username} / {self.email}>".format(self=self)
