
class Config(object):
    """
    Common configurations
    """

    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/sidharth/Documents/nbt/final/app/maps/database/locations_dev.db'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/sidharth/Documents/nbt/final/app/maps/database/locations.db'
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/sidharth/Documents/nbt/final/app/maps/database/locations_test.db'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}