from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://bulliq:bulliq@db:5432/bulliq"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)