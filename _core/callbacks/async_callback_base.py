from abc import (
    ABC,
    abstractmethod,
)
from typing import Any


class AsyncCallbackBase(ABC):
    async def __call__(self) -> Any:
        return await self._handle()

    @abstractmethod
    async def _handle(self) -> Any:
        pass
