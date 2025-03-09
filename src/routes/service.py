from fastapi import APIRouter, Depends
from http import HTTPStatus
from sqlalchemy.orm import Session

from src.crud import create_wallet, get_wallet, get_wallets, update_wallet, delete_wallet 
from src.crud import create_expense,get_expense, get_expenses, update_expense, delete_expense
from src.crud import create_income, get_income, get_incomes, update_income, delete_income
from src.database import get_db
from src.schemas import ExpenseSchema, IncomeSchema
from src.security import get_user_logged

router = APIRouter()

# Wallet routes
@router.post("/services/new-walltet", tags=["service"], status_code=HTTPStatus.CREATED)
def create_wallet_endpoint(wallet_name: str, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return create_wallet(db, wallet_name, user_logged)

@router.get("/services/wallets", tags=["service"], status_code=HTTPStatus.OK)
def get_wallets_endpoint(db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return get_wallets(db, user_logged)

@router.get("/services/wallets/{wallet_id}", tags=["service"], status_code=HTTPStatus.OK)
def get_wallet_endpoint(wallet_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return get_wallet(db, wallet_id, user_logged)

@router.put("/services/update-wallet", tags=["service"], status_code=HTTPStatus.OK)
def update_wallet_endpoint(wallet_id: int, wallet_name: str, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return update_wallet(db, wallet_id, wallet_name, user_logged)

@router.delete("/services/delete-wallet", tags=["service"], status_code=HTTPStatus.NO_CONTENT)
def delete_wallet_endpoint(wallet_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return delete_wallet(db, wallet_id, user_logged)

# Expense routes
@router.post("/services/{wallet_id}/new-expense", tags=["service"], status_code=HTTPStatus.CREATED)
def create_expense_endpoint(wallet_id: int, expense: ExpenseSchema, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return create_expense(db, wallet_id, expense)

@router.get("/services/{wallet_id}/expenses", tags=["service"], status_code=HTTPStatus.OK)
def get_expenses_endpoint(wallet_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return get_expenses(db, wallet_id)

@router.get("/services/{wallet_id}/expenses/{expense_id}", tags=["service"], status_code=HTTPStatus.OK)
def get_expense_endpoint(wallet_id: int, expense_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return get_expense(db, wallet_id, expense_id)

@router.put("/services/{wallet_id}/update-expense", tags=["service"], status_code=HTTPStatus.OK)
def update_expense_endpoint(wallet_id: int, expense_id: int, expense: ExpenseSchema, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return update_expense(db, wallet_id, expense_id, expense)

@router.delete("/services/{wallet_id}/delete-expense", tags=["service"], status_code=HTTPStatus.NO_CONTENT)
def delete_expense_endpoint(wallet_id: int, expense_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return delete_expense(db, wallet_id, expense_id)

# Income routes
@router.post("/services/{wallet_id}/new-income", tags=["service"], status_code=HTTPStatus.CREATED)
def create_income_endpoint(wallet_id: int, income: IncomeSchema, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return create_income(db, wallet_id, income)

@router.get("/services/{wallet_id}/incomes", tags=["service"], status_code=HTTPStatus.OK)
def get_incomes_endpoint(wallet_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return get_incomes(db, wallet_id)

@router.get("/services/{wallet_id}/incomes/{income_id}", tags=["service"], status_code=HTTPStatus.OK)
def get_income_endpoint(wallet_id: int, income_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return get_income(db, wallet_id, income_id)

@router.put("/services/{wallet_id}/update-income", tags=["service"], status_code=HTTPStatus.OK)
def update_income_endpoint(wallet_id: int, income_id: int, income: IncomeSchema, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return update_income(db, wallet_id, income_id, income)

@router.delete("/services/{wallet_id}/delete-income", tags=["service"], status_code=HTTPStatus.NO_CONTENT)
def delete_income_endpoint(wallet_id: int, income_id: int, db: Session = Depends(get_db), user_logged=Depends(get_user_logged)):
    return delete_income(db, wallet_id, income_id)