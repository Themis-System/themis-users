import pytest
from pytest import mark

from _core.models import User
from themis_users import create_user
from themis_users.exceptions import (
    DuplicateFieldException,
    EmptyOrNullFieldException,
)


@mark.asyncio
async def test_create_user_successfully():
    name = 'John'
    email = 'john.smith@example.com'
    username = 'john.smith'
    password = 'password_example'
    last_name = 'Smith'

    result_user = await create_user(
        name=name,
        email=email,
        username=username,
        password=password,
        last_name=last_name,
    )
    assert isinstance(result_user, User)

    user_obj = await User.get(id=result_user.id)
    assert user_obj.name == name
    assert user_obj.email == email
    assert user_obj.username == username
    assert user_obj.password == password
    assert user_obj.last_name == last_name


@mark.asyncio
async def test_create_user_with_empty_required_fields_raises_exception():
    with pytest.raises(EmptyOrNullFieldException) as exc_info:
        await create_user(
            name='',
            email='',
            username='',
            password='',
            last_name='',
        )

    expected_fields_err = ['name', 'email', 'username', 'password']
    expected_mss_err = f'The following fields are required and cannot be empty: {expected_fields_err}'
    assert expected_mss_err in str(exc_info.value)


@mark.asyncio
async def test_create_user_when_unique_fields_exist_in_user_model_raises_exception(default_user_constructor):
    with pytest.raises(DuplicateFieldException) as exc_info:
        await create_user(
            name=default_user_constructor.name,
            email=default_user_constructor.email,
            username=default_user_constructor.username,
            password=default_user_constructor.password,
            last_name=default_user_constructor.last_name,
        )

    expected_mss_err = 'A record with the provided value already exists for the field "username".'
    assert expected_mss_err in str(exc_info.value)
