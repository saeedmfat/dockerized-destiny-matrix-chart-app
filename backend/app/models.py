from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from .database import Base

class Calculation(Base):
    __tablename__ = "calculations"
    __table_args__ = {'schema': 'matrix_schema'}
    
    id = Column(Integer, primary_key=True, index=True)
    birth_day = Column(Integer)
    birth_month = Column(Integer)
    birth_year = Column(Integer)
    life_path_number = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)