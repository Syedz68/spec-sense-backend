from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")
    ENV: str = Field(..., env="ENV")
    VERSION: str = Field(..., env="VERSION")
    DEBUG: bool = Field(..., env="DEBUG")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(..., env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")
    ALLOWED_ORIGINS: list[str] = Field(..., env="ALLOWED_ORIGINS")
    LLM_API_ENCRYPTION_KEY: str = Field(..., env="LLM_API_ENCRYPTION_KEY")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., env="POSTGRES_PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()