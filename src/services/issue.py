from ast import List
from sqlalchemy.orm import Session
from src.models import Issue
from src.repositories import issue as issue_repo
from src.schemas import IssueCreate, IssueUpdate
from fastapi import HTTPException

def get_issue(db: Session, issue_id: int) -> Issue | None:
  issue = issue_repo.get_issue(db, issue_id)
  if not issue:
    raise HTTPException(status_code=404, detail="Issue not found")
  return issue

def get_issues(db: Session) -> List[Issue]:
  issues = issue_repo.get_issues(db)
  if not issues:
    raise HTTPException(status_code=404, detail="No issues found")
  return issues

def create_issue(db: Session, data: IssueCreate) -> Issue:
  issue = issue_repo.create_issue(db, data)
  if not issue:
    raise HTTPException(status_code=400, detail="Issue was not created")
  return issue

def update_issue(db: Session, issue_id: int, data: IssueUpdate) -> Issue:
  issue = issue_repo.update_issue(db, issue_id, data)
  if not issue:
    raise HTTPException(status_code=404, detail="Issue was not updated")
  return issue

def delete_issue(db: Session, issue_id: int) -> Issue:
  issue = issue_repo.delete_issue(db, issue_id)
  if not issue:
    raise HTTPException(status_code=404, detail="Issue was not deleted")
  return issue