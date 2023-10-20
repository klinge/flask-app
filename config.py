import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #: used for hashing and other things
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #: used for pagination
    POSTS_PER_PAGE = 10
    
    #: database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'microblog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #: flask login - set days for the 'remember me' cookie
    COOKIE_DURATION = timedelta(days=1)

    #: bootstrap config
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'
    BOOTSTRAP_BTN_STYLE = 'primary'
    BOOTSTRAP_BTN_SIZE = 'md'
    BOOTSTRAP_ICON_SIZE = '1em'
    BOOTSTRAP_ICON_COLOR = 'currentColor'

    #: mail settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['johan.klinge@dev.null']
    