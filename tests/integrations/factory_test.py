import uuid

from factory import Factory

from _core.models import User


class UserFactory(Factory):
    class Meta:
        model = User

    id = uuid.uuid4()
    created_at = '2025-01-01 12:00:00+00:00'
    modified_at = '2025-01-01 12:00:00+00:00'
    name = 'John'
    last_name = 'Smith'
    username = 'john.smith'
    email = 'john.smith@example.com'
    password = 'pass_example'
