from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

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

# -- Wallet schemas --
class WalletInDB(BaseModel):
    id: int
    wallet_name: str
    balance: float

class WalletResponse(BaseModel):
    wallet_name: str
    balance: float

# -- Category schemas --
class CategorySchema(BaseModel):
    category_name: str

class CategoryInDB(BaseModel):
    id: int
    category_name: str

# -- Expense schemas --
class Date(BaseModel):
    date: datetime.date

class ExpenseSchema(BaseModel):
    expense_name: str
    amount: float
    category_id: int
    wallet_id: int
    date: Date

# -- Income schemas --
class IncomeSchema(BaseModel):
    amount: float
    description: Optional[str]
    date: Date
    wallet_id: int