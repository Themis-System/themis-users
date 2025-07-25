import re

from tortoise.exceptions import IntegrityError

from _core.dtos.user_dto import CreateUserDTO
from _core.exceptions import DuplicateFieldException
from _core.models.user import User


class UserController:
    def __init__(self):
        self._model = User

    async def create_user(self, data: CreateUserDTO) -> 'User':
        try:
            return await self._model.create(
                name=data.name,
                username=data.username,
                email=data.email,
                password=data.password,
                last_name=data.last_name,
            )

        except IntegrityError as err:
            match = re.search(r'Key \((.*?)\)=', str(err))
            field_name = match.group(1) if match else 'unknown'
            mss_err = f'A record with the provided value already exists for the field "{field_name}".'
            raise DuplicateFieldException(mss_err)
