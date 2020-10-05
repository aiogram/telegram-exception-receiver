import asyncio

from pydantic import ValidationError
from sanic import response
from sanic.exceptions import InvalidUsage
from sanic.request import Request
from sanic.views import HTTPMethodView

from ..models import TelegramException


class ExceptionView(HTTPMethodView):
    async def post(self, request: Request):
        data = request.json
        if isinstance(data, list):
            unique_data = self._remove_duplicates(data)
            for obj in unique_data:
                self._process_exception(obj)
        else:
            self._process_exception(data)
        return response.text('OK')

    @staticmethod
    async def get(_: Request):
        exceptions = await TelegramException.get_all()
        return response.json(exceptions)

    @staticmethod
    def _process_exception(data: dict):
        try:
            exception = TelegramException(**data)
        except ValidationError as e:
            raise InvalidUsage(f"Data validation failed: {e}")

        asyncio.create_task(exception.save())

    @staticmethod
    def _remove_duplicates(data):
        return [dict(s) for s in set(frozenset(d.items()) for d in data)]
