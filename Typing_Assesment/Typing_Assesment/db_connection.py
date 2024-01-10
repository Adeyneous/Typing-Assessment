from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the base for the models
Base = declarative_base()

# Define the connection string for Windows Authentication
DATABASE_CONNECTION = (
    'mssql+pyodbc://DESKTOP-3V3FD81\MSSQLSERVER01/Emp_info'
    '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
)

# Create the database engine, which allows us to communicate with the database
engine = create_engine(DATABASE_CONNECTION, echo=True)

# Create a sessionmaker, which allows us to create sessions to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    # This will create the tables defined by your models
    Base.metadata.create_all(bind=engine)

def get_db_session():
    # Dependency that you can use to create a new database session
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

