class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "12345"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    ACL = 'public-read'
    FLASKS3_BUCKET_NAME = "murray-wagtail"
    AWS_ACCESS_KEY_ID = "AKIAWP7UQBNZ5V752LF6"
    AWS_SECRET_ACCESS_KEY = "NcfmfmnRH3Pck1uhiq7nHMPGXZe2qgbUuJrHyURU"

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    FLASKS3_BUCKET_DOMAIN = "s3-ap-southeast-2.amazonaws.com"
    FLASKS3_REGION = "ap-southeast-2"
    FLASKS3_ACTIVE = "True"
    FLASKS3_DEBUG = "True"

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False



