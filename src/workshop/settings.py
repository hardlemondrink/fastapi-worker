import os

from pydantic import BaseSettings

SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.getenv('SERVER_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

JWT_SECRET = os.getenv('JWT_SECRET')


class Settings(BaseSettings):
    server_host: str = SERVER_HOST
    server_port: int = SERVER_PORT
    database_url: str = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'

    jwt_secret: str = JWT_SECRET
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
