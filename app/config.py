

class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    #DB_Config
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.sqlite"



class ProductionConfig(Config):
    DEBUG=False
    "postgresql://username:password@localhost:portnumber/dbname"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@localhost:5432/iti"



app_config={
    'dev':DevelopmentConfig,
    'prd': ProductionConfig
}