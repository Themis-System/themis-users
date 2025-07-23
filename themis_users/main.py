from typing import Optional

from _core.callbacks import CreateUserCallback
from _core.dtos.user_dto import CreateUserDTO
from _core.models.user import User


async def create_user(
    name: str,
    username: str,
    email: str,
    password: str,
    last_name: Optional[str] = None,
) -> 'User':
    data_dto = CreateUserDTO(
        name=name,
        username=username,
        email=email,
        password=password,
        last_name=last_name,
    )
    callback = CreateUserCallback(data=data_dto)

    return await callback()
