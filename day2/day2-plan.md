# Day 2 - FastAPI Core (Upgraded)

Goal: Build a clean, structured REST API like real backend projects.

## 0:00-0:40
- Create structure: `routers/`, `models/`, `schemas/`.
- Add `routers/items.py` with list + create endpoints.
- Register router in `main.py`.

## 0:40-1:10
- Add Pydantic model `schemas/items.py`.
- Update create endpoint to use `Item` model.

## 1:10-1:40
- Add `GET /items/{item_id}` with 404 handling.
- Add query param `limit` to `GET /items`.

## 1:40-2:00
- Run app and test in Swagger.
- Commit and push.
