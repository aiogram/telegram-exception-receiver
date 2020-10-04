import asyncio

from pydantic import ValidationError
from sanic import response
from sanic.exceptions import InvalidUsage
from sanic.request import Request
from sanic.views import HTTPMethodView

from ..models import TelegramException


class ExceptionView(HTTPMethodView):
    @staticmethod
    async def post(request: Request):
        try:
            exception = TelegramException(**request.json)
        except ValidationError as e:
            raise InvalidUsage(f"Data validation failed: {e}")

        asyncio.create_task(exception.save())
        return response.text('OK')

    async def get(self, _: Request):
        exceptions = await TelegramException.get_all()
        return response.json(exceptions)
