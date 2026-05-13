from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    PORT: int = 4000
    CORS_ORIGIN: str = "http://localhost:5173"
    APP_MODE: str = "demo"
    CAMPUS_LAT: float = 4.8456717
    CAMPUS_LNG: float = -74.0300802
    QR_SECRET: str = "unicoc-demo-secret"

@lru_cache()
def get_settings():
    return Settings()
