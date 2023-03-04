""" Configuration file """
import os
import urllib.parse

# App details
APP_VERSION = '1.0.0'
APP_TITLE = 'Differnial Privacy Query Interface'
APP_DESCRIPTION = 'Provides a interface to users to Query in a database by adding noise to it to secure the privay of data.'

basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
FLASK_ENV = os.getenv('env', 'dev')

# Log config details
LOG_FOLDER_NAME = 'logs'
LOG_ERR_FILE_NAME = 'error.log'
LOG_FILE_NAME = 'dev.log'
LOG_WERKZEUG_FILE_NAME = 'werkzeug.log'
LOG_PATH = os.path.join(basedir, LOG_FOLDER_NAME)

class BaseConfig:
    """ Config class """
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'wiuj094jndo23h9rnd928hdn928339d82n'
    DB_DRIVER = 'ODBC Driver 17 for SQL Server'
    DB_HOST = os.getenv("host", "127.0.0.1")
    DB_NAME = os.getenv("dbname", "diff_privacy")
    DB_USERNAME = os.getenv("username", "root")
    DB_PASSWORD = os.getenv("password", "root")
    DB_PARAMS = urllib.parse.quote_plus(
        'DRIVER={' + DB_DRIVER + '};SERVER=' + DB_HOST + ';DATABASE=' + DB_NAME + ';UID=' + DB_USERNAME + ';PWD=' + DB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' % DB_PARAMS


class DevelopmentConfig(BaseConfig):
    """ DevelopmentConfig class """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ TestingConfig class for unit test cases"""
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """ ProductionConfig class """
    DEBUG = True


config_by_name = dict(
    local=DevelopmentConfig,
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    stage=ProductionConfig,
    test=TestingConfig
)

key = BaseConfig.SECRET_KEY
