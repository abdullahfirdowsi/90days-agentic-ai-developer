# Tuesday - FastAPI Core (Upgraded)

Goal: Build a clean, structured REST API like real backend projects.

You are not just learning syntax. You are learning architecture.

## 0:00-0:40 - CRUD endpoints with proper structure

Create folders:

```
ai-backend/
  main.py
  routers/
    items.py
  models/
    items.py
  schemas/
    items.py
```

Create router in `routers/items.py`:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

fake_db = []

@router.get("/")
def get_items():
    return fake_db

@router.post("/")
def create_item(item: dict):
    fake_db.append(item)
    return item
```

Register router in `main.py`:

```python
from fastapi import FastAPI
from routers import items

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "API running"}
```

## 0:40-1:10 - Pydantic models (professional validation)

Create `schemas/items.py`:

```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
```

Update router:

```python
from schemas.items import Item

@router.post("/")
def create_item(item: Item):
    fake_db.append(item.model_dump())
    return item
```

## 1:10-1:40 - Params + errors + status codes

Add:

```python
from fastapi import HTTPException, status

@router.get("/{item_id}")
def get_item(item_id: int):
    if item_id >= len(fake_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return fake_db[item_id]
```

Add query params:

```python
@router.get("/")
def get_items(limit: int = 10):
    return fake_db[:limit]
```

## 1:40-2:00 - Swagger testing + commit

Run:

```powershell
uvicorn main:app --reload
```

Open:

`http://127.0.0.1:8000/docs`

Test:

- Send wrong types
- Missing fields
- Invalid id

Then commit:

```powershell
git add .
git commit -m "Day 2: CRUD items API with validation"
git push
```

## Outcome

- REST API design
- Request validation
- Modular architecture
- Error handling
- Documentation generation
- Backend patterns used in real work

## Day 3 Preview

- Database integration (Neon CRUD)
- SQLAlchemy models
- Persistent storage
- Migrations
- Real data layer
