from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
  low = "low"
  medium = "medium"
  high = "high"

class Status(str, Enum):
  backlog = "backlog"
  up_next = "up_next"
  in_progress = "in_progress"
  done = "done"


class IssueBase(BaseModel):
  title: str = Field(max_length=255)
  description: str
  priority: Priority = Field(default=Priority.medium)
  status: Status = Field(default=Status.backlog)

class IssueCreate(IssueBase):
  pass

class IssueUpdate(IssueBase):
  title: str | None = Field(max_length=255)
  description: str | None = None
  priority: Priority | None = None
  status: Status | None = None
  updated_at: datetime

class IssueCompleted(IssueBase):
  pass

class IssueResponse(IssueBase):
  id: int
  created_at: datetime
  updated_at: datetime | None = None
  completed_at: datetime | None = None
  class Config:
    from_attributes = True