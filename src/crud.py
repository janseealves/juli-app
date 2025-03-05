from sqlalchemy.orm import Session
from .models import User
from .schemas import UserSchema

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserSchema):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_newname: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user_newname
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User deleted successfully"}
