# goldwheel-fastapi

## Create Project
```bash
poetry init

poetry add alembic tenacity httpx psycopg2-binary passlib 'python-jose[cryptography]' Jinja2 python-multipart 'pydantic[email]' pydantic-settings uvicorn fastapi SQLAlchemy

poetry add pytest flake8 --group dev
```

## Project Structure
```

```

## Usage
#### Install dependencies
```bash
poetry intall
```

#### initialize database data
```bash
poetry run python pestart.py
```
#### run server(watch mode)
```bash
poetry run ./run.py
```