from fastapi import APIRouter, Depends, Form, HTTPException 
from http import HTTPStatus
from sqlalchemy.orm import Session 

from src.database import get_db
from src.models import User
from src.security import create_access_token, verify_password

router = APIRouter()

@router.post("/auth", tags=["auth"], status_code=HTTPStatus.ACCEPTED)
def login(username: str=Form(...), password: str=Form(...), db: Session=Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid credentials")
    if not verify_password(password, db_user.password):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid credentials")
    return {
        "access_token": create_access_token(subject=db_user.username),
        "token_type": "bearer"
        }