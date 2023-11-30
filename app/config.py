#!/usr/bin/python3
# config.py
import os

# Flask configuration
DEBUG = True
SECRET_KEY = 'your_secret_key'

# Database configuration
CARIBA_MYSQL_USER = os.getenv('CARIBA_MYSQL_USER')
CARIBA_MYSQL_PWD = os.getenv('CARIBA_MYSQL_PWD')
CARIBA_MYSQL_HOST = os.getenv('CARIBA_MYSQL_HOST')
CARIBA_MYSQL_DB = os.getenv('CARIBA_MYSQL_DB')
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
    CARIBA_MYSQL_USER,
    CARIBA_MYSQL_PWD,
    CARIBA_MYSQL_HOST,
    CARIBA_MYSQL_DB)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Security configuration
SECURITY_PASSWORD_SALT = '146585145368132386173505678016728509634'
SECURITY_EMAIL_VALIDATOR_ARGS = {"check_deliverability": False}

# Add other configuration settings as needed

# Mail config
MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")


# Don't worry if email has findable domain
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_USERNAME_ENABLE = True
SECURITY_USERNAME_REQUIRED = True