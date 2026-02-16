# ai-backend

FastAPI starter with Neon Postgres.

## Setup

```powershell
Set-Location "c:\Projects\Personal\90d-dream\day1\task\ai-backend"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn pydantic psycopg[binary] python-dotenv
```

Create a `.env` file with your Neon connection string:

```env
DB_URL=postgresql://USER:PASSWORD@HOST:PORT/aidb?sslmode=require
```

## Run

```powershell
uvicorn main:app --reload
```

## Endpoints

- `GET /` -> Hello World
- `GET /db-check` -> database connectivity check
- `GET /tests` -> list rows from `public.test`
- `POST /tests` -> insert row, body: `{ "name": "value" }`
