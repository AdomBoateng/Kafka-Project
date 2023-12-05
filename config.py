from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MAIL_USERNAME = str
    MAIL_PASSWORD = str
    MAIL_FROM = str
    MAIL_PORT = int
    MAIL_SERVER = str
    MAIL_SSL_TLS = bool
    MAIL_STARTTLS = bool
    USE_CREDENTIALS = bool
    VALIDATE_CERTS = bool

    ############Kafka configuration############
    topic_name = str
    kafka_server = str

    class Config:
        env_file = ".env"

############Instantiate an object called settings from the class Settings###################
settings = Settings()