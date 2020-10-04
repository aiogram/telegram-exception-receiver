from typing import Optional

from sanic import Sanic

_app: Optional[Sanic] = None


def get_app(**kwargs) -> Sanic:
    global _app
    if isinstance(_app, Sanic):
        return _app

    _app = Sanic(name="ExceptionReceiver", **kwargs)
    _app.config.KEEP_ALIVE_TIMEOUT = 15
    return _app
