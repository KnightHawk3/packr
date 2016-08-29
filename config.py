from datetime import timedelta
import os
import logging


class Config(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ['SECRET_KEY']

    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_EXPIRATION_DELTA = timedelta(seconds=86400)
    JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)

    LOGGING_LEVEL = logging.INFO
    LOGGING_LOCATION = 'app.logs'


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG


class Production(Config):
    PRODUCTION = True
