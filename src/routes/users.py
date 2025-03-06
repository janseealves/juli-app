from fastapi import APIRouter, Depends
from http import HTTPStatus
from sqlalchemy.orm import Session

from src.schemas import Message, UserPublic, UsersResponse, UserSchema
from src.crud import get_users, get_user, create_user, update_user, delete_user
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users",tags=["user"], status_code=HTTPStatus.OK, response_model=UsersResponse)
def get_users_endpoint(db: Session=Depends(get_db)):
    return {"users": get_users(db)}

@router.get("/users/{user_id}",tags=["user"], status_code=HTTPStatus.OK, response_model=UserPublic)
def get_user_endpoint(user_id: int, db: Session=Depends(get_db)):
    return get_user(db, user_id)

@router.post("/users", tags=["user"], status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user_endpoint(user: UserSchema, db: Session=Depends(get_db)):
    return create_user(db, user)

@router.put("/users/{user_id}", tags=["user"], status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user_endpoint(user_id, user: UserSchema, db: Session=Depends(get_db)):
    return update_user(db, user_id, user)

@router.delete("/users/{user_id}", tags=["user"], status_code=HTTPStatus.OK, response_model=Message)
def delete_user_endpoint(user_id: int, db: Session=Depends(get_db)):
    return delete_user(db, user_id) 