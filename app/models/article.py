from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.core.database import Base

class Article(Base):
    __tablename__ = 'articles'

    id  = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __str__(self):
        return self.title