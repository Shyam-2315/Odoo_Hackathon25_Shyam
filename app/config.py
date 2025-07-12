from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str = "rewear_db"
    DB_USER: str = "rewear_user"
    DB_PASSWORD: str = "231505"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"

    @property
    def database_url(self):
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"  # Loads from .env file

settings = Settings()
