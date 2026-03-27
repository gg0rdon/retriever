from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
  issue_id: int
  body: str

class CommentCreate(CommentBase):
  created_at: datetime

class CommentUpdate(CommentBase):
  pass

class CommentResponse(CommentBase):
  id: int
  class Config:
    from_attributes = True