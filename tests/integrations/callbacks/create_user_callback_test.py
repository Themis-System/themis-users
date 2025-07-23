from pytest import mark

from _core.models import User
from themis_users import create_user


@mark.asyncio
async def test_create_user_callback_successfully(initialize_db):
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
