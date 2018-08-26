## MongoEngine Note: include db name in URI; it overwrites all others

class Config(object):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
