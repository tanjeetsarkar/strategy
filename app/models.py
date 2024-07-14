from sqlalchemy import create_engine, Column, Integer, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:example@localhost:5433/graphdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Node(Base):
    __tablename__ = "node"
    id = Column(Integer, primary_key=True, index=True)
    decision = Column(JSON)

class Link(Base):
    __tablename__ = "link"
    id = Column(Integer, primary_key=True, index=True)
    left = Column(Integer, ForeignKey("node.id"))
    right = Column(Integer, ForeignKey("node.id"))

class Rule(Base):
    __tablename__ = "rule"
    id = Column(Integer, primary_key=True, index=True)
    rule = Column(JSON)

