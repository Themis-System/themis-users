from _core.dtos.user_dto import CreateUserDTO
from _core.models.user import User


class UserController:
    def __init__(self):
        self._model = User

    async def create_user(self, data: CreateUserDTO) -> 'User':
        return await self._model.create(
            name=data.name,
            username=data.username,
            email=data.email,
            password=data.password,
            last_name=data.last_name,
        )
