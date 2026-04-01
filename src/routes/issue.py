from src.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from src.services import issue as issue_service
from src.schemas import IssueCreate, IssueUpdate, IssueResponse

router = APIRouter(prefix="/issues", tags=["Issues"])

@router.get("/", response_model=list[IssueResponse])
def get_issues(db: Session = Depends(get_db)):
  return issue_service.get_issues(db)

@router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
  return issue_service.get_issue(db, issue_id)

@router.post("/", response_model=IssueResponse)
def create_issue(data: IssueCreate, db: Session = Depends(get_db)):
  return issue_service.create_issue(db, data)

@router.patch("/{issue_id}", response_model=IssueResponse)
def update_issue(data: IssueUpdate, issue_id: int, db: Session = Depends(get_db)):
  return issue_service.update_issue(db, issue_id, data)

@router.delete("/{issue_id}", response_model=IssueResponse)
def delete_issue(issue_id: int, db: Session = Depends(get_db)):
  return issue_service.delete_issue(db, issue_id)
