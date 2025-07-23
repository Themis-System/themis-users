from _core.callbacks.async_callback_base import AsyncCallbackBase
from _core.controllers.user_controller import UserController
from _core.dtos.user_dto import CreateUserDTO
from _core.models.user import User


class CreateUserCallback(AsyncCallbackBase):
    def __init__(self, data: CreateUserDTO):
        self._data = data

    async def _handle(self) -> 'User':
        return await UserController().create_user(data=self._data)
