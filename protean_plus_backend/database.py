from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///protean.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

class QueryLog(Base):
    __tablename__ = "query_logs"
    id = Column(Integer, primary_key=True, index=True)
    query = Column(String)
    embedding = Column(String)

Base.metadata.create_all(bind=engine)
