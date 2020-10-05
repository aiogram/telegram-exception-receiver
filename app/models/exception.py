from datetime import datetime
from typing import Optional

from aiocache import cached
from pydantic import BaseModel

from ..core import mongo

CREATED = "created"
UPDATED = "updated"


def _cache_key(_, *args, **__):
    self = args[0]
    return hash(self)


class TelegramException(BaseModel):
    code: int
    name: str
    description: str
    created: Optional[datetime]
    updated: Optional[datetime]

    def __hash__(self):
        return hash(self.json(exclude={CREATED, UPDATED}))

    @cached(ttl=60, key_builder=_cache_key)
    async def save(self):
        db = mongo.get_database().get_collection("exceptions")
        now = datetime.now()
        search = self.dict(exclude={CREATED, UPDATED})
        update = {
            "$set": {UPDATED: now},
            '$setOnInsert': {'created': now},
        }
        await db.update_one(search, update, upsert=True)

    @classmethod
    @cached(ttl=10, noself=True)
    async def get_all(cls):
        db = mongo.get_database().get_collection("exceptions")
        all_data = await db.find({}).to_list(length=None)
        return [cls(**data).dict(exclude={CREATED, UPDATED}) for data in all_data]
