from os import getenv
# import os

DEBUG = True

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', None)
assert SQLALCHEMY_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"