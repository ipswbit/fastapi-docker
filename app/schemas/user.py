from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    """Схема для создания пользователя"""

    name: str
    age: int
    sex: str | None = None
    job: str | None = None


class UserRead(UserCreate):
    """Схема для чтения пользователя"""

    id: int
    model_config = ConfigDict(from_attributes=True)


class UserID(BaseModel):
    """Схема ответа с ID созданного пользователя"""

    ok: bool = True
    user_id: int
