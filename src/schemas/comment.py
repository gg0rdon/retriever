from pydantic import BaseModel, Field
from datetime import datetime

class CommentBase(BaseModel):
  body: str = Field(min_length=1, max_length=500)

class CommentCreate(CommentBase):
  issue_id: int
  pass

class CommentUpdate(BaseModel):
  body: str = Field(min_length=1, max_length=500)
  pass

class CommentResponse(CommentBase):
  id: int
  issue_id: int
  created_at: datetime
  class Config:
    from_attributes = True