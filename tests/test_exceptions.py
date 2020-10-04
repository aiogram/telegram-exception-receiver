import logging

import pytest  # noqa
from pytest_sanic.utils import TestClient

from app import web_app
from app.core import mongo

logger = logging.getLogger()

PATH = '/exception'


@pytest.yield_fixture(name='app')
async def app_fixture():
    yield web_app
    mongo.close()


@pytest.yield_fixture(name='test_cli')
async def test_cli_fixture(app, sanic_client):
    return await sanic_client(app)


async def test_post(test_cli: TestClient):
    data = {
        "code": 400,
        "name": 'BadRequest',
        "description": 'Something went wrong!',
    }
    resp = await test_cli.post(PATH, json=data)
    assert resp.status == 200


async def test_posts(test_cli: TestClient):
    data = [
        {
            "code": 402,
            "name": 'BadRequest',
            "description": 'Something went wrong again!',
        },
        {
            "code": 403,
            "name": 'VeryBadRequest',
            "description": 'Something went absolutely wrong!',
        },
    ]
    resp = await test_cli.post(PATH, json=data)
    assert resp.status == 200


async def test_get(test_cli: TestClient):
    resp = await test_cli.get(PATH)
    assert resp.status == 200
    print(await resp.json())
