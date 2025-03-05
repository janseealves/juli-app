from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy import DATE

registry = registry() # Registra metadados de classes mapeadas

@registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, not_null=True)
    email: Mapped[str] = mapped_column(unique=True, not_null=True)
    password: Mapped[str] = mapped_column(not_null=True)

class Category:
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(not_null=True)

class Expense:
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(foreign_key=User.id, not_null=True)
    amount: Mapped[float] = mapped_column(not_null=True)
    description: Mapped[str]
    date: Mapped[DATE] = mapped_column(not_null=True) #TODO: Verificar se é possível usar DATE
    category_id: Mapped[int] = mapped_column(foreign_key=Category.id, not_null=True)

class Income:
    __tablename__ = "incomes"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(foreign_key=User.id, not_null=True)
    amount: Mapped[float] = mapped_column(not_null=True)
    description: Mapped[str]
    date: Mapped[DATE] = mapped_column(not_null=True) #TODO: Verificar se é possível usar DATE

class Wallet:
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(foreign_key=User.id, not_null=True)
    balance: Mapped[float] = mapped_column(not_null=True)
    last_update: Mapped[DATE] = mapped_column(not_null=True) #TODO: Verificar se é possível usar DATE

class Wallet_User:
    __tablename__ = "wallet_users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(foreign_key=User.id, not_null=True)
    wallet_id: Mapped[int] = mapped_column(foreign_key=Wallet.id, not_null=True)
    is_owner: Mapped[bool] = mapped_column(not_null=True)