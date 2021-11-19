from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from typing import List

from models.tasks import (
    Task,
    TaskCreate,
)
from services.tasks import TaskService


router = APIRouter()


@router.get('/tasks', response_model=List[Task])
def get_tasks(service: TaskService = Depends()):
    return service.get_list()


@router.post('/new', response_model=TaskCreate)
def create_task(
    task_data: TaskCreate,
    service: TaskService = Depends(),
):
    return service.create(task_data)


@router.get('/id={task_id}', response_model=Task)
def get_task(
    task_id: int,
    service: TaskService = Depends(),
):
    return service.get(task_id)


@router.get('/done_id={task_id}', response_model=Task)
def done_task(
    task_id: int,
    service: TaskService = Depends(),
):
    return service.done(task_id)


@router.delete('/deleting_id={task_id}')
def delete_task(
    task_id: int,
    service: TaskService = Depends(),
):
    service.delete(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)