"""Модуль базовой модели."""
from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    """Базовая модель."""
