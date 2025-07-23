from _core.db import (
    close_db,
    initialize_db,
)


async def initialize() -> None:
    await initialize_db()


async def close() -> None:
    await close_db()
