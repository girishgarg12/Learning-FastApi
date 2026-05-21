from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:Ggsql@localhost:5432/FastApiDB"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)