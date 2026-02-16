from fastapi import APIRouter, HTTPException, status

from schemas.items import Item

router = APIRouter(prefix="/items", tags=["items"])

fake_db = []


@router.get("/")
def get_items(limit: int = 10):
    return fake_db[:limit]


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    fake_db.append(item.model_dump())
    return item


@router.get("/{item_id}")
def get_item(item_id: int):
    if item_id >= len(fake_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return fake_db[item_id]
