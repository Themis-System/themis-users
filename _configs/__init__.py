import os

from dotenv import load_dotenv


if not os.getenv('LOADED_ENV'):
    load_dotenv('.env')
    os.environ['LOADED_ENV'] = '1'

ENV = os.getenv('ENVIRONMENT', '').lower()

if ENV == 'development':
    from .env_development import *  # noqa: F401, F403
elif ENV == 'production':
    from .env_production import *  # noqa: F401, F403
else:
    if ENV:
        raise ValueError(f' The environment `{ENV}` is not set up.')
    else:
        raise ValueError(' The `.env` file was not found. Define the `ENVIRONMENT` variable correctly.')
