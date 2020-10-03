class Config(object):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    ACL = 'public-read'
    FLASKS3_BUCKET_NAME = "murray-wagtail"
    
    

  
  
    FLASK_APP = "app.py"
    FLASKS3_BUCKET_DOMAIN = "s3-ap-southeast-2.amazonaws.com"
    FLASKS3_REGION = "ap-southeast-2"
    FLASKS3_ACTIVE = "True"
    FLASKS3_DEBUG = "True"

   

    SESSION_COOKIE_SECURE = False




