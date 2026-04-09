from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Priority(str, Enum):
  """
  Enum for currently defined priorities.
  """
  low = "low"
  medium = "medium"
  high = "high"

class Status(str, Enum):
  """
  Enum for currently defined statuses.
  """
  backlog = "backlog"
  up_next = "up_next"
  in_progress = "in_progress"
  done = "done"


class IssueBase(BaseModel):
  """
  Base issue schema consists of title,
  description,
  priority,
  status,
  """
  title: str = Field(max_length=255)
  description: str
  priority: Priority = Field(default=Priority.medium)
  status: Status = Field(default=Status.backlog)

class IssueCreate(IssueBase):
  """
  Create schema validates data for a new issue.
  """
  pass

class IssueUpdate(IssueBase):
  """
  Update demands a lot of optional fields because the smallest update is still an update.
  """
  title: str | None = Field(default=None, max_length=255)
  description: str | None = None
  priority: Priority | None = None
  status: Status | None = None
  updated_at: datetime

class IssueCompleted(IssueBase):
  """
  Completed schema validates data for a completed issue.
  """
  pass

class IssueResponse(IssueBase):
  """
  Response schema demands all information
  """
  id: int
  created_at: datetime
  updated_at: datetime | None = None
  completed_at: datetime | None = None
  class Config:
    from_attributes = True
