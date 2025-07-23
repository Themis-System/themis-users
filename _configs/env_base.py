import os


# Database Postgres
DB_NAME = os.environ['DB_NAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_PORT = os.environ['DB_PORT']
DB_URL = os.environ['DB_URL']
DB_USER = os.environ['DB_USER']

# Database Postgres Test
TEST_DB_NAME = 'db_themis_users_test'
TEST_DB_PASSWORD = 'password_themis_users_test'
TEST_DB_PORT = 5435
TEST_DB_URL = 'localhost'
TEST_DB_USER = 'user_themis_users_test'
