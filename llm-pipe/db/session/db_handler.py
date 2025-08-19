from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL_PATH = "postgresql+psycopg2://timescaledb:timescaledb@timescaledb:5432/alerts_db"
database_engine = create_engine(DATABASE_URL_PATH)
session = sessionmaker(bind=database_engine,autoflush=False,autocommit=False)

Base = declarative_base()


