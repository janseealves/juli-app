from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    name: str
    email: EmailStr

class UsersResponse(BaseModel):
    users: list[UserPublic]
