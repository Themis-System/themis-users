# themis-users

Microservice for user management within the Themis System application.

---

## Requirements

- Python `>=3.12`
- Poetry `>=2.1.3`
- Docker
- Docker Compose

---

## Project Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Themis-System/themis-users.git
   cd themis-users
   ```

2. Create the `.env` file:
   ```bash
   cp .env.example .env
   ```

3. Initialize the virtual environment for the project:
   ```bash
   poetry shell
   ```

4. Initialize the virtual environment for the project and install dependencies:
   ```bash
   poetry install
   ```

---

## Environment Variables

Correctly configure the `.env` file:

```env
ENVIRONMENT=development

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_URL=localhost
DB_PORT=
```

---

## Development Environment

1. Start the PostgreSQL test database using Docker Compose:
   ```bash
   docker compose -f docker-compose.test.yml up -d
   ```

2. Install pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

3. (Optional) Run all pre-commit hooks manually:
   ```bash
   poetry run pre-commit run --all-files
   ```

---

## Poetry Usage

- Add a package (production):

  ```bash
  poetry add <package-name>
  ```

- Add a development-only package:

  ```bash
  poetry add --group dev <package-name>
  ```

- List all installed dependencies:

  ```bash
  poetry show
  ```

- Update dependencies:

  ```bash
  poetry update
  ```

---

## Running Tests

Run the test suite:

- Run tests with Poetry:
  ```bash
  poetry run pytest
  ```

- (Optional) Run integration tests:
  ```bash
  poetry run pytest tests/integrations
  ```

- (Optional) Or run a specific test:
  ```bash
  poetry run pytest tests/<route-test>::<name-specific-test>
  ```

- Or if you are inside a virtual environment:
  ```bash
  pytest
  ```

## Shutting Down Test Database

To stop and remove the PostgreSQL test container when you are done:

```bash
docker compose -f docker-compose.test.yml down
```

This will gracefully shut down the test database container and remove associated resources.
