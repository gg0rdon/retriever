from src.models import Comment
from sqlalchemy.orm import Session
from src.schemas import CommentCreate
from src.schemas.comment import CommentUpdate

def get_comment(db: Session, comment_id: int) -> Comment | None:
  return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comments_by_issue(db: Session, issue_id: int) -> list[Comment] | None:
  return db.query(Comment).filter(Comment.issue_id == issue_id).all()

def create_comment(db: Session, issue_id: int, data: CommentCreate) -> Comment:
  comment = Comment(issue_id, **data.model_dump())
  db.add(comment)
  db.commit()
  db.refresh(comment)
  return comment

def update_comment(db: Session, comment_id: int, data: CommentUpdate) -> Comment | None:
  comment = get_comment(db, comment_id)
  if not comment:
    return None
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(comment, field, value)
  db.commit()
  db.refresh(comment)
  return comment

def delete_comment(db: Session, comment_id: int) -> Comment | None:
  comment = get_comment(db, comment_id)
  if not comment:
    return None
  db.delete(comment)
  db.commit()
  return comment

