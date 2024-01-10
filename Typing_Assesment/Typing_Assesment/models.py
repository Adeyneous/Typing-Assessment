from sqlalchemy import Column, Integer, String
from .db_connection import Base

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    # add other fields as per your requirements
