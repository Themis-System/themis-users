import uuid

import asyncpg
from pytest_asyncio import fixture
from tortoise import Tortoise

from _configs import (
    TEST_DB_NAME,
    TEST_DB_PASSWORD,
    TEST_DB_PORT,
    TEST_DB_URL,
    TEST_DB_USER,
)
from tests.integrations.factory_test import UserFactory


@fixture(scope='function', autouse=True)
async def initialize_db():
    db_name = f'test_db_{uuid.uuid4().hex[:8]}'
    admin_url = f'postgres://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_URL}:{TEST_DB_PORT}/{TEST_DB_NAME}'

    conn = await asyncpg.connect(admin_url)
    await conn.execute(f'CREATE DATABASE "{db_name}" TEMPLATE "{TEST_DB_NAME}"')
    await conn.close()

    db_url = f'postgres://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_URL}:{TEST_DB_PORT}/{db_name}'
    await Tortoise.init(db_url=db_url, modules={'models': ['_core.models']})
    await Tortoise.generate_schemas()

    yield

    await Tortoise.close_connections()
    conn = await asyncpg.connect(admin_url)
    await conn.execute(f'DROP DATABASE IF EXISTS "{db_name}"')
    await conn.close()


@fixture
async def default_user_constructor():
    user_obj = await UserFactory.build()
    await user_obj.save()
    return user_obj
