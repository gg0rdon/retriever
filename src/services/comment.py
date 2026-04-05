from src.models import Comment
from sqlalchemy.orm import Session
from src.repositories import comment as comment_repo
from src.schemas import CommentCreate, CommentUpdate
from fastapi import HTTPException

def get_comment(db: Session, comment_id: int) -> Comment:
  """
  Get comment by id and returns it to the router or raise an error.
  :param db: Current database session.
  :param comment_id: Comment identifier.
  :return: The fetched comment object.
  """
  comment = comment_repo.get_comment(db, comment_id)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment not found")
  return comment

def get_comments_by_issue(db: Session, issue_id: int) -> list[Comment]:
  """
  Get all comments for a specific issue or raise an error.
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :return: All the listed comments for the issue.
  """
  comments = comment_repo.get_comments_by_issue(db, issue_id)
  if not comments:
    raise HTTPException(status_code=404, detail="Comments not found")
  return comments

def create_comment(db: Session, issue_id: int, data: CommentCreate) -> Comment:
  """
  Creates a comment and raise an issues if it couldn't
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :param data: Validated create comment data from the request body.
  :return: The new comment object.
  """
  comment = comment_repo.create_comment(db, issue_id, data)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment creation failed")
  return comment

def update_comment(db: Session, comment_id: int, data: CommentUpdate) -> Comment:
  """
  Update an existing comment or raise an error if it couldn't
  :param db: Current database session.
  :param comment_id: Comment identifier.
  :param data: Validated update comment data from the request body.
  :return: The updated comment object.
  """
  comment = comment_repo.update_comment(db, comment_id, data)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment update failed")
  return comment

def delete_comment(db: Session, comment_id: int) -> Comment:
  """
  Deletes an existing comment by id amd raise an error if it couldn't
  :param db: Current database session.
  :param comment_id: Comment identifier.
  :return: The deleted comment object.
  """
  comment = comment_repo.delete_comment(db, comment_id)
  if not comment:
    raise HTTPException(status_code=404, detail="Comment was not deleted")
  return comment