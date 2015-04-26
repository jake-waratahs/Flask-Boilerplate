from .Base import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))

    # Relationship to all this category's posts
    posts = relationship('BlogPost')
    posts_lazy = relationship('BlogPost', lazy='dynamic') # Define a lazy relationship to allow dynamic queries on children.