import asyncio

from sanic import response
from sanic.request import Request
from sanic.views import HTTPMethodView

from ..models import TelegramException


class ExceptionView(HTTPMethodView):
    @staticmethod
    async def post(request: Request):
        exception = TelegramException(**request.json)
        # asyncio.create_task(exception.save())
        await exception.save()
        return response.text('OK')

    async def get(self, _: Request):
        exceptions = await TelegramException.get_all()
        return response.json(exceptions)
