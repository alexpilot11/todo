from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/todos/list")
def todo_list():
    pass


@app.post("/todos/create")
def create_todo():
    pass


@app.put("/todos/update")
def update_todo():
    pass

