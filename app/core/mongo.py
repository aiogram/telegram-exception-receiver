from typing import Optional

from motor.core import Database
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from pymongo import ReadPreference

from .yaml import get_cfg

cfg = get_cfg('mongo')

_client: Optional[AsyncIOMotorClient] = None


def get_client() -> MongoClient:
    """
    Returns mongodb async client instance.

    We should use only one client instance per app.
    Every instance have a pool of connections.

    :rtype: AioMongoClient
    """
    global _client

    # existing instance
    if isinstance(_client, AsyncIOMotorClient):
        return _client

    # create new
    uri = cfg.get('uri')
    if uri is None:
        user = cfg.get('user')
        password = cfg.get('password')
        host = cfg.get('host')
        uri = f'mongodb://{user}:{password}@{host}'
    _client = AsyncIOMotorClient(uri)
    return _client


def get_database(db_name='exceptions', read_preference=ReadPreference.SECONDARY_PREFERRED):
    """
    Returns database instance.

    Usage:
        >>> result = await db.collection_name.find_one_and_update(...)

    :param db_name: database name
    :param read_preference: Primary? Secondary?
    :type db_name: str
    :rtype: Database
    """
    client = get_client()
    db = client.get_database(db_name, read_preference=read_preference)
    return db


def close():
    global _client
    client = get_client()
    client.close()
    _client = None
