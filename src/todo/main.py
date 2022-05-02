from fastapi import FastAPI
from typing import Optional

from todo.routers import todo
from todo.fake_db.items import items


app = FastAPI()

app.include_router(todo.router)


@app.get("/")
def read_root():
    """say hello!"""
    return {"Hello": "World"}


@app.get("/items")
def read_items(q: Optional[str] = None):
    """get list of items"""
    # TODO: is there a faster way to do this?
    return (
        items
        if not q
        else [item for item in items if q.lower() in item["name"].lower()]
    )


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """get one item"""
    returnable = None
    for item in items:
        if item["id"] == item_id:
            returnable = item
    return returnable
