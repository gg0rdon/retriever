from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Issue
from src.schemas import IssueCreate, IssueResponse, IssueUpdate
from src.services import issue as issue_service

# The specific issue router for viewing, creating ,updating and deleting issues
issue_router = APIRouter(prefix="/issue", tags=["Issues"])

@issue_router.get("/", response_model=list[IssueResponse])
def get_issues(db: Session = Depends(get_db)) -> list[Issue]:
  """
  Get all issues router which is dependent on the database session.
  :param db: Current database session.
  :return: A list of all issues it found.
  """
  return issue_service.get_issues(db)

@issue_router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(issue_id: int, db: Session = Depends(get_db)) -> Issue:
  """
  Get issue router for a given issue, depends on the database session.
  :param issue_id: Issue identifier.
  :param db: Current database session.
  :return: A Issue object.
  """
  return issue_service.get_issue(db, issue_id)

@issue_router.post("/", response_model=IssueResponse)
def create_issue(data: IssueCreate, db: Session = Depends(get_db)) -> Issue:
  """
  Create issue router which depends on the database session.
  :param data: Validated create issue data from the request body.
  :param db: Current database session.
  :return: A new created Issue object.
  """
  return issue_service.create_issue(db, data)

@issue_router.patch("/{issue_id}", response_model=IssueResponse)
def update_issue(data: IssueUpdate, issue_id: int, db: Session = Depends(get_db)) -> Issue:
  """
  Update issue router which depends on the database session.
  :param data: Validated update issue data from the request body.
  :param issue_id: Issue identifier.
  :param db: Current database session.
  :return: A updated Issue object.
  """
  return issue_service.update_issue(db, issue_id, data)

@issue_router.delete("/{issue_id}", response_model=IssueResponse)
def delete_issue(issue_id: int, db: Session = Depends(get_db)) -> Issue:
  """
  Delete issue router which depends on the database session.
  :param issue_id: Issue identifier.
  :param db: Current database session.
  :return: Deleted Issue object.
  """
  return issue_service.delete_issue(db, issue_id)
