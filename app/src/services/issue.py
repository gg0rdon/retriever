from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models import Issue
from src.repositories import issue as issue_repo
from src.schemas import IssueCreate, IssueUpdate


def get_issue(db: Session, issue_id: int) -> Issue:
  """
  Get issues by id or raise an error.
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :return: The fetched issue.
  """
  issue = issue_repo.get_issue(db, issue_id)
  if not issue:
    raise HTTPException(status_code=404, detail="Issue not found")
  return issue

def get_issues(db: Session) -> list[Issue]:
  """
  Get all issues currently listed or raise an error.
  :param db: Current database session.
  :return: A list of issues.
  """
  issues = issue_repo.get_issues(db)
  if not issues:
    raise HTTPException(status_code=404, detail="No issues found")
  return issues

def create_issue(db: Session, data: IssueCreate) -> Issue:
  """
  Create a new issue or raise an error if it couldn't
  :param db: Current database session.
  :param data: Validated create issue data from the request body.
  :return: The new issue object.
  """
  issue = issue_repo.create_issue(db, data)
  if not issue:
    raise HTTPException(status_code=400, detail="Issue was not created")
  return issue

def update_issue(db: Session, issue_id: int, data: IssueUpdate) -> Issue:
  """
  Updates an existing issue or raise an error if it couldn't
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :param data: Validated update issue data from the request body.
  :return: The updated issue object.
  """
  issue = issue_repo.update_issue(db, issue_id, data)
  if not issue:
    raise HTTPException(status_code=404, detail="Issue was not updated")
  return issue

def delete_issue(db: Session, issue_id: int) -> Issue:
  """
  Delete an existing issue by id or raise an error if it couldn't
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :return: The deleted issue object.
  """
  issue = issue_repo.delete_issue(db, issue_id)
  if not issue:
    raise HTTPException(status_code=404, detail="Issue was not deleted")
  return issue
