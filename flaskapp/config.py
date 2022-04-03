import json


# opens the file in specified path
with open('/etc/ocr_config.json') as f:
    config = json.load(f)


# for production / live
class Productoin:
    # flask
    SECRET_KEY = config.get('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    # domain
    SERVER_NAME = config.get('SERVER_NAME')


# for when developing / testing
class Development:
    # flask
    SECRET_KEY = config.get('SECRET_KEY')
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False
    # domain
    SERVER_NAME = config.get('SERVER_NAME')
