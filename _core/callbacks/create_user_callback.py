from _core.callbacks.async_callback_base import AsyncCallbackBase
from _core.controllers.user_controller import UserController
from _core.dtos.user_dto import CreateUserDTO
from _core.models.user import User
from _core.utils.validate_data import validate_field_is_null_or_empty


class CreateUserCallback(AsyncCallbackBase):
    def __init__(self, data: CreateUserDTO):
        self._data = data

    def _validate(self):
        required_fields = ['name', 'email', 'username', 'password']
        validate_field_is_null_or_empty(required_fields=required_fields, data=self._data)

    async def _handle(self) -> 'User':
        return await UserController().create_user(data=self._data)
