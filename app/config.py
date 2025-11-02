from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Base de données
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/soiladvisor_db"
    
    # Application
    APP_NAME: str = "SoilAdvisor"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # API
    API_PORT: int = 8000
    API_HOST: str = "0.0.0.0"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()