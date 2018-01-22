import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ABSOLUTE_PATH = os.path.join(BASE_DIR, 'app/maps/database/')


class Config(object):
    """
    Common configurations
    """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ABSOLUTE_PATH, 'locations_dev.db')
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ABSOLUTE_PATH, 'locations.db')

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ABSOLUTE_PATH, 'locations_test.db')



app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}