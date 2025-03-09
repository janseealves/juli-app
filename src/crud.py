from fastapi import HTTPException
from http import HTTPStatus
from sqlalchemy import func
from sqlalchemy.orm import Session
from .models import Category, User, Wallet, WalletUser, Expense, Income
from .schemas import  Date, ExpenseSchema, IncomeSchema, UserSchema
from .security import hashed_password

# CRUD operations for User
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
    
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password(user.password)
    )
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

# CRUD operations for Wallet
def create_wallet(db: Session, wallet_name: str, user_logged: User):
   # TODO: Implementar verificação se o usua´rio já possui uma carteira com esse nome.
    wallet = Wallet(wallet_name=wallet_name)
    db.add(wallet)
    db.commit()
    db.refresh(wallet)

    wallet_user = WalletUser(user_id=user_logged.id, wallet_id=wallet.id)
    db.add(wallet_user)
    db.commit()
    db.refresh(wallet_user)

    return {
        "Id": wallet.id, 
        "Name": wallet.wallet_name,
        "Owner": user_logged.username,
        }

def get_wallets(db: Session, user_logged: User):
    wallets = db.query(Wallet).join(WalletUser).filter(WalletUser.user_id == user_logged.id).all()
    return wallets

def get_wallet(db: Session, wallet_id: int, user_logged: User):
    wallet = db.query(Wallet).join(WalletUser).filter(Wallet.id == wallet_id, WalletUser.user_id == user_logged.id).first()
    if not wallet:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Wallet not found")
    return wallet

def update_wallet(db: Session, wallet_id: int, wallet_name: str, user_logged: User):
    wallet = db.query(Wallet).join(WalletUser).filter(Wallet.id == wallet_id, WalletUser.user_id == user_logged.id).first()

    if not wallet:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Wallet not found")
    if wallet.wallet_name == wallet_name:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Wallet name already exists")

    wallet.wallet_name = wallet_name
    db.commit()
    db.refresh(wallet)
    return wallet

def delete_wallet(db: Session, wallet_id: int, user_logged: User):
    wallet = db.query(Wallet).join(WalletUser).filter(Wallet.id == wallet_id, WalletUser.user_id == user_logged.id).first()

    if not wallet:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Wallet not found")

    db.delete(wallet)
    db.commit()
    return {"message": "Wallet deleted successfully"}

# CRUD operations for Category
def get_categories(db: Session):
    categories = db.query(Category).all()
    return categories

def create_category(db: Session, category_name: str):
    category = db.query(Category).filter(Category.category_name == category_name).first()

    if category:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Category already exists") 
    category = Category(category_name=category_name)

    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, category_id: int, category_name: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Category not found")
    category.name = category_name
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message": "Category deleted successfully"}

# CRUD operations for Expense
def get_expenses(db: Session, wallet_id: int):
    expenses = db.query(Expense).filter(Expense.wallet_id == wallet_id).all()
    return expenses

def get_expense(db: Session, expense_id: int, wallet_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.wallet_id == wallet_id).first()
    if not expense:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Expense not found")
    return expense

def create_expense(db: Session, expense: ExpenseSchema):
    # TODO: Implementar uma lógica para que não seja necessário passar o wallet_id
    expense = Expense(
        expense_name=expense.expense_name,
        amount=expense.amount,
        category_id=expense.category_id,
        date=expense.date,
        wallet_id=expense.wallet_id
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    db.commit()
    return expense

def update_expense(db: Session, expense_id: int, expense_category: str, expense_amount: float, expense_date: Date):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Expense not found")
    expense.expense_name = expense.expense_name
    expense.amount = expense.amount
    expense.category_id = expense.category_id
    expense.date = expense.date
    db.commit()
    db.refresh(expense)
    return expense

def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}

# CRUD operations for Income
def get_incomes(db: Session, wallet_id: int):
    incomes = db.query(Income).filter(Income.wallet_id == wallet_id).all()
    return incomes

def get_income(db: Session, income_id: int, wallet_id: int):
    income = db.query(Income).filter(Income.id == income_id, Income.wallet_id == wallet_id).first()
    if not income:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Income not found")
    return income

def create_income(db: Session, income: IncomeSchema):
    income = Income(
        amount=income.amount,
        description=income.description,
        date=income.date,
        wallet_id=income.wallet_id
    )
    db.add(income)
    db.commit()
    db.refresh(income)
    return income

def update_income(db: Session, income_id: int, income_amount: float, income_description: str, income_date: Date):
    income = db.query(Income).filter(Income.id == income_id).first()
    if not income:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Income not found")
    income.amount = income.amount
    income.description = income.description
    income.date = income.date
    db.commit()
    db.refresh(income)
    return income

def delete_income(db: Session, income_id: int):
    income = db.query(Income).filter(Income.id == income_id).first()
    if not income:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Income not found")
    db.delete(income)
    db.commit()
    return {"message": "Income deleted successfully"}