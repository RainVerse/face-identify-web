import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:100200@localhost:3306/machinelearning"


# 测试环境
class TestingConfig(Config):
    TESTING = True


# 生产环境
class ProductionConfig(Config):
    PRODUCTION = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
