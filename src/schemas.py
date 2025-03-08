from pydantic import BaseModel, EmailStr
from typing import Optional

class Message(BaseModel):
    message: str

# -- Token schemas --
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# -- User schemas --
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    username: str
    email: EmailStr

class UsersResponse(BaseModel):
    users: list[UserPublic]
