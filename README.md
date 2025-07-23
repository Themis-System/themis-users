# themis-users

<p>
  <img src="_assets/Themis-Users-Logo-Red.png" alt="Themis Users Logo" width="150"/>
</p>
Microservice for user management within the Themis System application.

---

## ⚙️ Requirements

- Python `>=3.12`
- Poetry `>=2.1.3`
- Docker
- Docker Compose

---

## 📦 Project Installation

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

4. Install dependencies:
   ```bash
   poetry install
   ```

---

## 🔐 Environment Variables

Configure the `.env` file:

```env
ENVIRONMENT=development

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_URL=localhost
DB_PORT=
```

---

## 🧮    Development Environment

1. Start the PostgreSQL test database:
   ```bash
   docker compose -f docker-compose.test.yml up -d
   ```

2. Install pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

3. (Optional) Run all pre-commit hooks:
   ```bash
   poetry run pre-commit run --all-files
   ```

---

##  🧰 Poetry Usage

- Add a package (production):

  ```bash
  poetry add <package-name>
  ```

- Add a dev-only package:

  ```bash
  poetry add --group dev <package-name>
  ```

- List dependencies:

  ```bash
  poetry show
  ```

- Update all dependencies:

  ```bash
  poetry update
  ```

---

## 🧪 Running Tests

Run the test suite:

- With Poetry:
  ```bash
  poetry run pytest
  ```

- Run integration tests:
  ```bash
  poetry run pytest tests/integrations
  ```

- Run a specific test:
  ```bash
  poetry run pytest tests/<route-test>::<name-specific-test>
  ```

- Inside virtual env:
  ```bash
  pytest
  ```

---

## 🧹 Shutting Down Test Database

Stop and remove the test DB container:

```bash
docker compose -f docker-compose.test.yml down
```
