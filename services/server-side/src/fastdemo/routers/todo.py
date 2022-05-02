from fastapi import APIRouter

router = APIRouter()


@router.get("/todos/list")
def todo_list():
    pass


@router.post("/todos/create")
def create_todo():
    pass


@router.put("/todos/update")
def update_todo():
    pass

