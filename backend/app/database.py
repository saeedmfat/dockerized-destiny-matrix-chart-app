from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "postgresql://matrix_user:securepassword123@localhost/destiny_matrix?options=-csearch_path%3Dmatrix_schema"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Calculation(Base):
    __tablename__ = "calculations"
    
    id = Column(Integer, primary_key=True, index=True)
    birth_day = Column(Integer)
    birth_month = Column(Integer)
    birth_year = Column(Integer)
    life_path_number = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)