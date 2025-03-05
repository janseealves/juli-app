from sqlalchemy.orm import Mapped, mapped_column, registry

registry = registry()

@registry.mapped_as_dataclass

class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]