import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
  """
  Fetches the local session and closes it once the fetch is done.
  Does a rollback on any exception raised during the session.
  """
  db = session_local()
  try:
    yield db
  except Exception:
    db.rollback()
    raise
  finally:
    db.close()
