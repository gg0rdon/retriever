from pydantic import BaseModel, Field
from datetime import datetime

class CommentBase(BaseModel):
  """
  Base schema for comment which demands the issue identifier and the body text.
  """
  body: str = Field(min_length=1, max_length=500)

class CommentCreate(CommentBase):
  """
  Create schema validates data for a new comment.
  """
  pass

class CommentUpdate(CommentBase):
  """
  Update schema validates data for the comment to be updated.
  """
  pass

class CommentResponse(CommentBase):
  """
  Response schema demands all information
  """
  id: int
  issue_id: int
  created_at: datetime
  class Config:
    from_attributes = True