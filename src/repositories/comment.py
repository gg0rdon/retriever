from src.models import Comment
from sqlalchemy.orm import Session
from src.schemas import CommentCreate
from src.schemas.comment import CommentUpdate

def get_comment(db: Session, comment_id: int) -> Comment | None:
  """
  Fetch a comment from the database of given comment id.
  :param db: The current database session.
  :param comment_id: Comment identifier.
  :return: Suppose to be Comment or None, not type[Comment].
  """
  return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comments_by_issue(db: Session, issue_id: int) -> list[Comment]:
  """
  Fetches all comments for given issue id.
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :return: list of Comment objects.
  """
  return db.query(Comment).filter(Comment.issue_id == issue_id).all()

def create_comment(db: Session, issue_id: int, data: CommentCreate) -> Comment:
  """
  Creates a new comment related to a specific issue.
  :param db: Current database session.
  :param issue_id: Issue identifier.
  :param data: Related info to the Comment object, see Comment model.
  :return: A new Comment object from the database.
  """
  comment = Comment(issue_id, **data.model_dump())
  db.add(comment)
  db.commit()
  db.refresh(comment)
  return comment

def update_comment(db: Session, comment_id: int, data: CommentUpdate) -> Comment | None:
  """
  In case a comment should receive an update in its description.
  :param db: Current database session.
  :param comment_id: Comment identifier.
  :param data: Validated comment data from the request body
  :return: A existing newly updated Comment object or None if no object was found.
  """
  comment = get_comment(db, comment_id)
  if not comment:
    return None
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(comment, field, value)
  db.commit()
  db.refresh(comment)
  return comment

def delete_comment(db: Session, comment_id: int) -> Comment | None:
  """
  In case a comment is not desired any more.
  :param db: Current database session.
  :param comment_id: Comment identifier.
  :return: A Comment object or None if no object was found.
  """
  comment = get_comment(db, comment_id)
  if not comment:
    return None
  db.delete(comment)
  db.commit()
  return comment

