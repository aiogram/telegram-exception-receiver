from datetime import datetime
from typing import Optional

from aiocache import cached
from pydantic import BaseModel

from ..core import mongo

CREATED = "created"
UPDATED = "updated"


class TelegramException(BaseModel):
    code: int
    name: str
    description: str
    created: Optional[datetime]
    updated: Optional[datetime]

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
        print(all_data)
        return [cls(**data).dict(exclude={CREATED, UPDATED}) for data in all_data]
