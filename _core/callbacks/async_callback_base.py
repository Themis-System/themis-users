from abc import (
    ABC,
    abstractmethod,
)
from typing import Any


class AsyncCallbackBase(ABC):
    async def __call__(self) -> Any:
        return await self._run_callback()

    async def _run_callback(self) -> Any:
        if hasattr(self, '_validate') and callable(getattr(self, '_validate')):
            self._safe_validate()
        return await self._handle()

    def _safe_validate(self) -> None:
        try:
            self._validate()
        except NotImplementedError:
            pass

    def _validate(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def _handle(self) -> Any:
        pass
