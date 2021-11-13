from pydantic import BaseSettings 
#Parsing-Bibliothek, welche die Basis-Einstellungen der Datenbank festlegt

class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str

    class Config:
        env_file = ".env"
        
#Basis-Einstellungen der Datenbank