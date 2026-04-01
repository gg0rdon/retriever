from src.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from src.services import comment as comment_service
from src.schemas import CommentCreate, CommentUpdate, CommentResponse

router = APIRouter(prefix="/issues/{issue_id}/comments", tags=["comments"])

@router.get("/", response_model=list[CommentResponse])
def get_issue_comments(issue_id: int, db: Session = Depends(get_db)):
  return comment_service.get_comments_by_issue(db, issue_id)

@router.post("/", response_model=CommentResponse)
def create_comment(issue_id: int, data: CommentCreate, db: Session = Depends(get_db)):
  return comment_service.create_comment(db, issue_id, data)

@router.patch("/{comment_id}", response_model=CommentResponse)
def update_comment(issue_id: int, comment_id: int, data: CommentUpdate, db: Session = Depends(get_db)):
  return comment_service.update_comment(db, comment_id, data)

@router.delete("/{comment_id}", response_model=CommentResponse)
def delete_comment(issue_id: int, comment_id: int, db: Session = Depends(get_db)):
  return comment_service.delete_comment(db, comment_id)
