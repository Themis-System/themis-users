from typing import Optional

from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    name: str
    username: str
    email: str
    password: str
    last_name: Optional[str] = None
