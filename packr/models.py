# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from packr.database import (Column, Model, SurrogatePK, db, reference_col,
                            relationship)
from packr.extensions import bcrypt


class Role(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)


class User(SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime,
                        nullable=False,
                        default=dt.datetime.utcnow)
    firstname = Column(db.String(30), nullable=True)
    lastname = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=True)
    is_admin = Column(db.Boolean(), default=False)
    is_driver = Column(db.Boolean(), default=False)

    business_account = db.Column(db.Boolean, nullable=True, default=False)

    # orders = db.relationship('Order', backref='user', lazy='joined')

    def __init__(self, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self,
                          email=email,
                          **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def verify_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.firstname, self.lastname)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)
