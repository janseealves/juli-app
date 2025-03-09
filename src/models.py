from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry
from datetime import datetime
from src.database import engine

registry = registry() # Registra metadados de classes mapeadas

@registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, not_null=True)
    email: Mapped[str] = mapped_column(unique=True, not_null=True)
    password: Mapped[str] = mapped_column(not_null=True)
    created_at: Mapped[datetime] = mapped_column(init=False)

@registry.mapped_as_dataclass
class Wallet:
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    wallet_name: Mapped[str] = mapped_column(not_null=True)
    # TODO: Pensar em uma feature de mapear despesas e investimentos, para melhorar a visualização da distribuição do saldo.
    balance: Mapped[float] = mapped_column(init=False, default=0.0)

@registry.mapped_as_dataclass
class WalletUser:
    __tablename__ = "wallets_users"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"), primary_key=True)

@registry.mapped_as_dataclass
class Category:
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    category_name: Mapped[str] = mapped_column(unique=True, not_null=True)

@registry.mapped_as_dataclass
class Expense: 
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    amount: Mapped[float] = mapped_column(not_null=True)
    description: Mapped[str]
    date: Mapped[datetime] = mapped_column(not_null=True) # TODO: Verificar se é possível usar o tipo datetime
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))

@registry.mapped_as_dataclass
class Income:
    __tablename__ = "incomes"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    amount: Mapped[float] = mapped_column(not_null=True)
    description: Mapped[str]
    date: Mapped[datetime] = mapped_column(not_null=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))

registry.metadata.create_all(engine)
