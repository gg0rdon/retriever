from sqlalchemy.orm import Session
from src.models import Issue
from src.schemas import IssueBase, IssueCreate
from typing import List

from src.schemas.issue import IssueUpdate


def get_issue(db: Session, issue_id: int):
  return db.query(Issue).filter(Issue.id == issue_id).first()

def get_issues(db: Session):
  return db.query(Issue).all()

def create_issue(db: Session, data: IssueCreate):
  issue = Issue(**data.model_dump())
  db.add(issue)
  db.commit()
  db.refresh(issue)
  return issue

def update_issue(db: Session, issue_id: int, data: IssueUpdate):
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(issue, field, value)
  db.commit()
  db.refresh(issue)
  return issue

def delete_issue(db: Session, issue_id: int):
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  db.delete(issue)
  db.commit()
  return issue

