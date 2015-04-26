from .Base import Base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    String,
    DateTime,
    Boolean,
)
from sqlalchemy.orm import relationship
from .Label import label_post
import datetime

class BlogPost(Base):
    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    title = Column(String(255))
    created = Column(DateTime, default=datetime.datetime.now())
    is_visible = Column(Boolean, default=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')

    labels = relationship('Label', secondary=label_post)
    labels_lazy = relationship('Label', secondary=label_post, lazy='dynamic')