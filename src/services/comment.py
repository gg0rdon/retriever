from ast import List
from src.models import Comment
from sqlalchemy.orm import Session
from src.repositories import comment as comment_repo
from src.schemas import CommentCreate, CommentUpdate
from fastapi import HTTPException

def get_comment(db: Session, comment_id: int) -> Comment:
  comment = comment_repo.get_comment(db, comment_id)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment not found")
  return comment

def get_comments_by_issue(db: Session, issue_id: int) -> List[Comment]:
  comments = comment_repo.get_comments_by_issue(db, issue_id)
  if not comments:
    raise HTTPException(status_code=404, detail="Comments not found")
  return comments

def create_comment(db: Session, issue_id: int, data: CommentCreate) -> Comment:
  comment = comment_repo.create_comment(db, issue_id, data)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment creation failed")
  return comment

def update_comment(db: Session, comment_id: int, data: CommentUpdate) -> Comment:
  comment = comment_repo.update_comment(db, comment_id, data)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment update failed")
  return comment

def delete_comment(db: Session, comment_id: int) -> Comment:
  comment = comment_repo.delete_comment(db, comment_id)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment was not deleted")
  return comment