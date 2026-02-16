import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

def main():
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise SystemExit("DB_URL not set in .env")

    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, created_at FROM public.test ORDER BY id LIMIT 10;")
            rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
