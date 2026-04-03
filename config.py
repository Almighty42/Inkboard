import os

class BaseConfig:
    APP_NAME = "Inkboard"
    DEBUG = False
    TESTING = False
    # SECRET_KEY

    # HOST = os.getenv("HOST", "127.0.0.1")
    HOST = "Example"
    # PORT = int(os.getenv("PORT", 3001))
    PORT = 3001

config = BaseConfig()
