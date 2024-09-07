from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://proj3_user:o8yib48fkeFPVyWhYX4CtU1G3sTOtva9@dpg-cre2r3ggph6c73emcv10-a.oregon-postgres.render.com/proj3"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
