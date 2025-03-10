from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from http import HTTPStatus
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError
from sqlalchemy.orm import Session
import os
from typing import Optional

from src.database import get_db
from src.models import User

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=30

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/auth")

pwd_context = CryptContext(schemes=["sha256_crypt"])

def hashed_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: Optional[str]=None): #Subject is the username of the user
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

class TokenPayLoad(BaseModel):
    sub: Optional[int]=None

def get_user_logged(token: str=Depends(reusable_oauth2), db: Session=Depends(get_db)):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        token_data = TokenPayLoad(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid token")
    user = db.query(User).filter(User.username == token_data.sub).first()
    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user