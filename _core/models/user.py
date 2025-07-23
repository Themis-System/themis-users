import uuid

from tortoise import (
    Model,
    fields,
)


class User(Model):
    id = fields.UUIDField(primary_key=True, default=uuid.uuid4())
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    name = fields.CharField(max_length=120)
    last_name = fields.CharField(max_length=120, null=True)
    username = fields.CharField(max_length=120, unique=True)
    email = fields.CharField(max_length=120, unique=True)
    password = fields.CharField(max_length=120)
