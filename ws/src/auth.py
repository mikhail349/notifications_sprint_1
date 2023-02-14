"""Модуль авторизации."""
from http import HTTPStatus

import jwt
from fastapi import Depends
from fastapi.exceptions import WebSocketException
from jwt.exceptions import InvalidTokenError

from src import messages as msg
from src.config import jwt_settings
from src.models import User

jwt_public_key = open(jwt_settings.public_key_path).read()  # noqa: WPS515


def raise_no_access():
    """Функция вызова WebSocketException 403.

    Raises:
        WebSocketException: FORBIDDEN 403
    """
    raise WebSocketException(
        code=HTTPStatus.FORBIDDEN,
        reason=msg.NO_ACCESS,
    )


def decode_jwt(token: str) -> dict:
    """Расшифровать JWT.

    В случае ошибки вызывает HTTPException с кодом 403.

    Args:
        token: токен

    Returns:
        dict: payload

    """
    try:
        return jwt.decode(
            token,
            jwt_public_key,
            algorithms=[jwt_settings.algorithm],
        )
    except InvalidTokenError:
        raise_no_access()
        return {}  # mypy: Missing return statement  [return]


def login_required(token: str) -> User:
    """Dependency-функция авторизации пользователя.

    В случае ошибки вызывает HTTPException с кодом 403.

    Args:
        token: токен

    Returns:
        User: пользователь

    """
    decoded = decode_jwt(token)
    return User(
        username=decoded['sub'],
        is_superuser=decoded.get('is_superuser', False),
        permissions=decoded.get('permissions'),
    )


def permission_required(permission_name: str):
    """Dependency-функция проверки прав.

    Args:
        permission_name: название права

    Returns:
        Callable: основную функцию проверки прав

    """
    def inner(user: User = Depends(login_required)) -> User:  # noqa: WPS430
        """Основная функция проверки прав.

        В случае ошибки вызывает HTTPException с кодом 403.

        Args:
            user: пользователь

        Returns:
            User: пользователь

        """
        if not user.is_superuser:
            if permission_name not in user.permissions:
                raise_no_access()
        return user
    return inner


def superuser_required(user: User = Depends(login_required)) -> User:
    """Dependency-функция проверки прав суперпользователя.

    В случае ошибки вызывает HTTPException с кодом 403.

    Args:
        user: пользователь

    Returns:
        User: пользователь

    """
    if not user.is_superuser:
        raise_no_access()
    return user
