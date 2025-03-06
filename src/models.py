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

registry.metadata.create_all(engine)
