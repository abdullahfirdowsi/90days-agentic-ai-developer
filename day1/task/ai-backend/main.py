import os

import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()

app = FastAPI()


class TestItemIn(BaseModel):
    name: str


def get_db_url() -> str:
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise HTTPException(status_code=500, detail="DB_URL not set")
    return db_url


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    db_url = get_db_url()

    try:
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()
    except psycopg.Error as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {"ok": True, "result": result[0]}


@app.get("/tests")
def list_tests():
    db_url = get_db_url()

    try:
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, created_at FROM public.test ORDER BY id LIMIT 100;"
                )
                rows = cur.fetchall()
    except psycopg.Error as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return [
        {"id": row[0], "name": row[1], "created_at": row[2].isoformat()}
        for row in rows
    ]


@app.post("/tests")
def create_test(item: TestItemIn):
    db_url = get_db_url()

    try:
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO public.test (name) VALUES (%s) "
                    "RETURNING id, name, created_at;",
                    (item.name,),
                )
                row = cur.fetchone()
                conn.commit()
    except psycopg.Error as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {"id": row[0], "name": row[1], "created_at": row[2].isoformat()}
