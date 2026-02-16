# Day 3 - Async + Neon Database

Goal: Connect FastAPI to PostgreSQL properly using Neon.

## 0:00-0:20
- Get Neon connection string.
- Ensure it uses `postgresql+asyncpg://` and `ssl=require`.
- Create `.env` with `DATABASE_URL`.
- Ensure `.env` is in `.gitignore`.

## 0:20-1:00
- Install: `sqlalchemy`, `asyncpg`, `alembic`, `python-dotenv`.
- Create `database/db.py` and `database/models.py`.
- Define async engine and session.
- Define `User` model.

## 1:00-1:30
- Initialize Alembic.
- Wire `alembic/env.py` to load `DATABASE_URL` and `Base.metadata`.
- Autogenerate and apply migration.

## 1:30-1:50
- Create `schemas/users.py` and `routers/users.py`.
- Add `POST /users` and `GET /users/{id}`.
- Register router in `main.py`.

## 1:50-2:00
- Run app and test in Swagger.
- Verify rows exist in Neon.
- Commit and push.
