from .Base import Base
from sqlalchemy import (
    Column,
    Integer,
    Table,
    String
)
from sqlalchemy.orm import relationship

label_post = Table('label_post',
    Column('label_id', Integer, ForeignKey('label.id')),
    Column('post_id', Integer, ForeignKey('blog_post.id'))
)

class Label(Base):
    __tablename__ = 'label'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))

    # Relationship to all this category's items
    posts = relationship('BlogPost', secondary=label_post)
    posts_lazy = relationship('BlogPost', secondary=label_post, lazy='dynamic')
