from pydantic import BaseModel

from _core.exceptions import EmptyOrNullFieldException


def validate_field_is_null_or_empty(required_fields: list, data: BaseModel) -> None:
    fields_err = []
    for field in required_fields:
        value = getattr(data, field, None)
        if value is None or str(value).strip() == '':
            fields_err.append(field)
    if fields_err:
        raise EmptyOrNullFieldException(f'The following fields are required and cannot be empty: {fields_err}')
