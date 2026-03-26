from src import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship

class Issue(Base):
  __tablename__ = 'issues'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(255), nullable=False)
  description = Column(Text, nullable=False)
  status = Column(String(64), nullable=False)
  priority = Column(String(64), nullable=False)
  created_at = Column(DateTime, default=func.now())
  updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
  completed = Column(DateTime, nullable=False, default=False)
  comment = relationship("Comment", back_populates="issue", cascade="all, delete")