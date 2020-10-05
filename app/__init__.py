from asyncio import AbstractEventLoop

from sanic import Sanic
from sanic.log import logger

from .core import sanic
from .views import ExceptionView

web_app = sanic.get_app()
web_app.add_route(ExceptionView.as_view(), '/exception')


@web_app.listener('after_server_start')
async def after_server_start(_: Sanic, __: AbstractEventLoop):
    logger.warning('Server successfully started!')


@web_app.listener('after_server_stop')
async def after_server_stop(_: Sanic, __: AbstractEventLoop):
    from .core import mongo
    mongo.close()
    logger.warning('Stopped.')
