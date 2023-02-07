"""Модуль подключения к хранилищу уведомлений."""
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from motor import motor_asyncio

from src.config.mongo import mongo_config
from src.storages.mongo import Collection, MongoNotificationStorage


def create_notification_storage() -> MongoNotificationStorage:
    """Создать хранилище уведомлений MongoDB.

    Returns:
        MongoNotificationStorage: хранилище уведомлений MongoDB

    """
    url = 'mongodb://{username}:{password}@{host}:{port}'.format(
        username=mongo_config.username,
        password=mongo_config.password,
        host=mongo_config.host,
        port=mongo_config.port,
    )
    client = motor_asyncio.AsyncIOMotorClient(url)
    db = client[mongo_config.db]
    collection = db.get_collection(
        name=Collection.NOTIFICATIONS,
        codec_options=CodecOptions(
            uuid_representation=UuidRepresentation.STANDARD,
        ),
    )
    return MongoNotificationStorage(collection=collection)
