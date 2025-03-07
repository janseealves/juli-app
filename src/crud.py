from fastapi import HTTPException
from http import HTTPStatus
from sqlalchemy import func
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserSchema

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserSchema):
    username_exists = db.query(User).filter(User.username == user.username).first()
    if username_exists:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Username already exists")
    
    email_exists = db.query(User).filter(User.email == user.email).first()
    if email_exists:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Email already exists")
    
    db_user = User(**user.model_dump())
    db_user.created_at = func.now()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user= UserSchema):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    
    username_exists = db.query(User).filter(User.username == user.username, User.id != user_id).first()
    if username_exists:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Username already exists")
    
    email_exists = db.query(User).filter(User.email == user.email, User.id != user_id).first()
    if email_exists:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Email already exists")
    
    # db_user = User(**user.model_dump()) This will create a new user
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user
    
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
