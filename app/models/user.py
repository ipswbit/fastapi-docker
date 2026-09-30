from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class User(Base):
    """Модель пользователя."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    age: Mapped[int]
    sex: Mapped[str | None]
    job: Mapped[str | None]
