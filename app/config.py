from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str

    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    @property
    def DATABASE_URL(self) -> str:
        password = quote_plus(self.DB_PASS)
        return f"mysql+mysqlconnector://{self.DB_USER}:{password}@{self.DB_HOST}:3306/{self.DB_NAME}"

    class Config:
        env_file = "db.env"   

settings = Settings()
