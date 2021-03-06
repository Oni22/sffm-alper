from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import Settings


settings = Settings()
SQLALCHEMY_DATABASE_URL = "postgresql://" + settings.DB_USER + ":" + settings.DB_PASS + "@" + settings.DB_HOST + ":" + settings.DB_PORT + "/" + settings.DB_NAME

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBModel = declarative_base()
