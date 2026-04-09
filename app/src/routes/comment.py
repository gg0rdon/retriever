from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Comment
from src.schemas import CommentCreate, CommentResponse, CommentUpdate
from src.services import comment as comment_service

# The specific comment router for a specific issue
comment_router = APIRouter(prefix="/issues/{issue_id}/comments", tags=["comments"])

@comment_router.get("/", response_model=list[CommentResponse])
def get_issue_comments(issue_id: int, db: Session = Depends(get_db)) -> list[Comment]:
  """
  Get comments per issue router which is dependent on the database session.
  :param issue_id: issue identifier.
  :param db: Current database session.
  :return: A list of all comments objects related to given issue
  """
  return comment_service.get_comments_by_issue(db, issue_id)

@comment_router.post("/", response_model=CommentResponse)
def create_comment(issue_id: int, data: CommentCreate, db: Session = Depends(get_db)) -> Comment:
  """
  Create comment router which is dependent on the database session.
  :param issue_id: Issue identifier.
  :param data: Validated create comment data from request body.
  :param db: Current database session.
  :return: The newly created comment object
  """
  return comment_service.create_comment(db, issue_id, data)

@comment_router.patch("/{comment_id}", response_model=CommentResponse)
def update_comment(issue_id: int, comment_id: int, data: CommentUpdate, db: Session = Depends(get_db)) -> Comment:
  """
  Update comment router which is dependent on the database session.
  :param issue_id: Issue identifier.
  :param comment_id: Comment Identifier
  :param data: Validated update comment data from request body.
  :param db: Current database session.
  :return: The updated comment object
  """
  return comment_service.update_comment(db, comment_id, data)

@comment_router.delete("/{comment_id}", response_model=CommentResponse)
def delete_comment(issue_id: int, comment_id: int, db: Session = Depends(get_db)) -> Comment:
  """
  Delete comment router which is dependent on the database session.
  :param issue_id: Issue identifier.
  :param comment_id: Comment Identifier
  :param db: Current database session.
  :return: The deleted comment object
  """
  return comment_service.delete_comment(db, comment_id)
