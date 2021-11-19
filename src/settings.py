import os

from pydantic import BaseSettings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = "sqlite:///" + os.path.join(BASE_DIR, "database.sqlite3")


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)