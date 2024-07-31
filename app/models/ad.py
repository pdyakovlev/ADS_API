from sqlalchemy import Column, Integer, String

from app.core.db import Base


class Ad(Base):
    __tablename__ = 'ad'
    header = Column(String(60), nullable=False)
    id = Column('id', Integer, primary_key=True, nullable=False)
    author = Column(String(60), unique=False, nullable=False)
    views = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
