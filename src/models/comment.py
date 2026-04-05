from src import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Comment(Base):
  """
  The model for the Comments tabel
  Nothing extra here but an ordinary comment.
  Id: To identify each comment.
  body: The core part of the comment.
  issue_id: The issue related to the comment.
  created_at: Standard and good to know.
  issue: Creates the relation.
  """
  __tablename__ = 'comments'
  id = Column(Integer, primary_key=True, index=True)
  body = Column(Text, nullable=False)
  issue_id = Column(Integer, ForeignKey('issues.id', ondelete='CASCADE'), nullable=False)
  created_at = Column(DateTime, default=func.now())
  updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
  issue = relationship("Issue", back_populates="comments")
