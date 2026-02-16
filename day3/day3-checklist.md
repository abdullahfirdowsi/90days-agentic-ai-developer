# Wednesday - Async + Neon Database

Goal: FastAPI + async SQLAlchemy connected to Neon.

## 0:00-0:20 - Neon setup

- Copy Neon connection string.
- Must use `postgresql+asyncpg://` and `ssl=require`.
- Add `.env` with `DATABASE_URL=...`.
- Confirm `.env` is ignored by git.

## 0:20-1:00 - Async database layer

- Install: `sqlalchemy`, `asyncpg`, `alembic`, `python-dotenv`.
- Create `database/db.py` and `database/models.py`.
- Define async engine and session maker.
- Add `User` model.

## 1:00-1:30 - Alembic migration

- Run `alembic init alembic`.
- Update `alembic/env.py` to load `.env` and set `target_metadata`.
- Run:
  - `alembic revision --autogenerate -m "create users table"`
  - `alembic upgrade head`

## 1:30-1:50 - API endpoints

- Create `schemas/users.py` and `routers/users.py`.
- Add `POST /users` and `GET /users/{id}`.
- Register router in `main.py`.

## 1:50-2:00 - Test + commit

- Run: `uvicorn main:app --reload`.
- Test in Swagger:
  - `POST /users`
  - `GET /users/{id}`
- Commit:
  - `git add .`
  - `git commit -m "Day 3: Neon async database integration"`
  - `git push`

## Outcome

- Async API with real cloud DB
- Migrations in place
- Persistent data
