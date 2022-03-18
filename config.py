import os

class Config:
    '''
    General configuration parent class
    '''
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY='bubbles'
    DATABASE_URL='postgresql+psycopg2://postgres:o7oKanyi@localhost:5000/blogs'
    UPLOADED_PHOTOS_DEST ='app/static'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace('postgres://', 'postgresql://')

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:o7oKanyi@localhost/blog'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:o7oKanyi@localhost/blogs'

    DEBUG = True
    ENV = 'production'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
