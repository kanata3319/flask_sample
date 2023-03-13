"""FlaskのConfigを提供する"""
class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = '\xf7\xf4\x9bb\xd7\xa8\xdb\xee\x9f\xe3\x98SR\xda\xb0@\xb7\x12\xa4uB\xda\xa3\x1b'
    STRIPE_API_KEY = ''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
        'user': 'swim_user',
        'password': 'swim_pass',
        'host': '127.0.0.1',
        'name': 'flask_db'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
