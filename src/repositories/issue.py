from sqlalchemy.orm import Session
from src.models import Issue
from src.schemas import IssueCreate, IssueUpdate

def get_issue(db: Session, issue_id: int) -> Issue | None:
  return db.query(Issue).filter(Issue.id == issue_id).first()

def get_issues(db: Session) -> list[Issue] | None:
  return db.query(Issue).all()

def create_issue(db: Session, data: IssueCreate) -> Issue:
  issue = Issue(**data.model_dump())
  db.add(issue)
  db.commit()
  db.refresh(issue)
  return issue

def update_issue(db: Session, issue_id: int, data: IssueUpdate) -> Issue | None:
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(issue, field, value)
  db.commit()
  db.refresh(issue)
  return issue

def delete_issue(db: Session, issue_id: int) -> Issue | None:
  issue = get_issue(db, issue_id)
  if not issue:
    return None
  db.delete(issue)
  db.commit()
  return issue

