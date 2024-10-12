import os
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')



def factory(app):
    configuation = {
        'testing': TestConfig,
    }
    return configuation[app]