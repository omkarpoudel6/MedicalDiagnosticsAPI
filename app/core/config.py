from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #APP_NAME: str = "MedicalDiagnostics"
    #ENV: str = "development"
    #PORT: int = 8000
    
    APP_NAME: str
    ENV: str
    PORT: int
    
    class Config:
        env_file = ".env"
        
settings = Settings()