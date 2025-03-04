from fastapi import APIRouter, Depends
from http import HTTPStatus
from sqlalchemy.orm import Session

from src.schemas import UserPublic, UsersResponse, UserSchema
from src.crud import get_users, get_user, create_user
from src.database import Base, engine, SessionLocal

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users",tags=["user"], status_code=HTTPStatus.OK, response_model=UsersResponse)
def get_users_endpoint(db: Session=Depends(get_db)):
    return {"users": get_users(db)}

@router.get("/user/{user_id}",tags=["user"], status_code=HTTPStatus.OK, response_model=UserPublic)
def get_user_endpoint(user_id: int, db: Session=Depends(get_db)):
    return get_user(db, user_id)

@router.post("/user", tags=["user"], status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user_endpoint(user: UserSchema, db: Session=Depends(get_db)):
    return create_user(db, user)
