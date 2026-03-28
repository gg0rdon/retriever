from src import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Comment(Base):
  __tablename__ = 'comment'
  id = Column(Integer, primary_key=True, index=True)
  body = Column(Text, nullable=False)
  issue_id = Column(Integer, ForeignKey('issues.id'), ondelete='CASCADE')
  created_at = Column(DateTime, default=func.now())
  issue = relationship("Issue", back_populates="comment")
