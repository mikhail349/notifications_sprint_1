"""Модуль с фикструами объектов хранилищ."""
import uuid

import pytest

from src.storages.models.review import Review
from tests.functional.src.mocks import constants, factory, storages


@pytest.fixture
def review(data_storage: storages.MockedDataStorage) -> Review:
    """Фикстура рецензии.

    Args:
        data_storage: фикстура хранилища данных

    Returns:
        Review: рецензия

    """
    review = factory.create_review(
        id=constants.REVIEW_ID,
        author_username=constants.REVIEW_AUTHOR,
    )
    data_storage.add_review(review)
    return review


@pytest.fixture
def cohort(data_storage: storages.MockedDataStorage) -> str:
    """Фикстура когорты всех пользователей.

    Args:
        data_storage: фикстура хранилища данных

    Returns:
        str: название когорты

    """
    users = [factory.create_user() for _ in range(2)]
    data_storage.add_cohort(
        name=constants.COHORT_NAME,
        users=users,
    )
    return constants.COHORT_NAME


@pytest.fixture
def template(config_storage: storages.MockedConfigStorage) -> uuid.UUID:
    """Фикстура шаблона.

    Args:
        config_storage: фикстура хранилища настроек

    Returns:
        UUID: ИД шаблона

    """
    config_storage.add_template(
        id=constants.TEMPLATE_ID,
        template=constants.TEMPLATE,
    )
    return constants.TEMPLATE_ID
