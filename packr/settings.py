# -*- coding: utf-8 -*-
"""Application configuration."""
import logging
import os
from datetime import timedelta


class Config(object):
    """Base configuration."""

    # TODO: Change me
    SECRET_KEY = os.environ.get('PACKR_SECRET', 'ayylmao')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_EXPIRATION_DELTA = timedelta(seconds=86400)
    JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)

    LOGGING_LEVEL = logging.DEBUG
    LOGGING_LOCATION = 'app.logs'
    DEBUG = True


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    LOGGING_LEVEL = logging.DEBUG


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4
