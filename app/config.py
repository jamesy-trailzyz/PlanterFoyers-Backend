from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    DB_USER: str = "root"
    DB_PASS: str = "Admin@2025"
    DB_HOST: str = "localhost"
    DB_NAME: str = "PFResort"

    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  

    @property
    def DATABASE_URL(self) -> str:
        safe_password = quote_plus(self.DB_PASS)  # Encode special chars
        return f"mysql+mysqlconnector://{self.DB_USER}:{safe_password}@{self.DB_HOST}:3306/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()
