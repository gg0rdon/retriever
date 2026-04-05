from sqlalchemy import func
from sqlalchemy.orm import Session

from src.models import Issue
from src.schemas import IssueCreate, IssueUpdate

def get_issue(db: Session, issue_id: int) -> Issue | None:
  """
  Fetches an issue object from the database if it finds any.
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :return: The Issue object from the database or None if issue was not found.
  """
  issue = db.query(Issue).filter(Issue.id == issue_id).first()
  if not issue:
    return None
  return issue

def get_issues(db: Session) -> list[Issue] | None:
  """
  Fetches all issues from the database.
  :param db: Current database session.
  :return: A list of all the issues found from the database or None.
  """
  issues = db.query(Issue).all()
  if not issues:
    return None
  return issues

def create_issue(db: Session, data: IssueCreate) -> Issue:
  """
  Creates a new issue in the database.
  :param db: Current database session.
  :param data: Validated issue data from the request body
  :return: A new Issue object from the database.
  """
  issue = Issue(**data.model_dump())
  db.add(issue)
  db.commit()
  db.refresh(issue)
  return issue

def update_issue(db: Session, issue_id: int, data: IssueUpdate) -> Issue | None:
  """
  Updates an existing issue in the database.
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :param data: Validated issue data from the request body
  :return: A newly updated Issue object from the database or None if issue was not found.
  """
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(issue, field, value)
  db.commit()
  db.refresh(issue)
  return issue

def complete_issue(db: Session, issue_id: int, data: IssueUpdate) -> Issue | None:
  """
  The final move of an issue to completed.
  :param db: Current database session.
  :param issue_id: issue identifier.
  :param data: Validated issue data from the request body
  :return: The Issue object recently moved to done or None if issue was not found..
  """
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  issue.completed_at = func.now()
  db.add(issue)
  db.commit()
  db.refresh(issue)
  return issue

def delete_issue(db: Session, issue_id: int) -> Issue | None:
  """
  Simply deletes an issue from the database.
  :param db: Current database session.
  :param issue_id: issue identifier.
  :return: The recently deleted Issue object from the database or None if issue was not found..
  """
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  db.delete(issue)
  db.commit()
  return issue

