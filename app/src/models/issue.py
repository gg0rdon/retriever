from sqlalchemy import Column, DateTime, Integer, String, Text, func
from sqlalchemy.orm import relationship

from src import Base


class Issue(Base):
  """
  The model for issues table
  This is the core part of this simple issue tracker.
  id: To identify the issue.
  title: Short description of the issue.
  description: More detailed description of the issue.
  stats: If its in the backlog, in progress or even done.
  priority: High|Medium|Low
  created_at: Standard and good to know.
  updated_at: Will most likely receive updates often
  completed_at: Just for fun and I could watch back.
  comment: Relation to the comments tables
  """
  __tablename__ = 'issues'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(255), nullable=False)
  description = Column(Text, nullable=False)
  status = Column(String(64), nullable=False)
  priority = Column(String(64), nullable=False)
  created_at = Column(DateTime, default=func.now())
  updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
  completed_at = Column(DateTime, nullable=True, default=None)
  comments = relationship("Comment", back_populates="issue", cascade="all, delete")
