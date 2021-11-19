import tables

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from typing import List
from sqlalchemy.orm import Session

from database import get_session
from models.tasks import TaskCreate


class TaskService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Task]:
        query = (
            self.session
            .query(tables.Task)
        )
        tasks = query.all()
        return tasks

    def create(self, task_data: TaskCreate) -> tables.Task:
        task = tables.Task(**task_data.dict())
        self.session.add(task)
        self.session.commit()
        return task

    def get(self, task_id: int) -> tables.Task:
        task = (
            self.session
            .query(tables.Task)
            .filter_by(id=task_id)
            .first()
        )
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"Error": "This id doesn't exist"}
            )
        return task
    
    def done(self, task_id: int) -> tables.Task:
        task = self.get(task_id)
        setattr(task, "is_done", True)
        self.session.commit()
        return task


    def delete(self, task_id: int) -> tables.Task:
        task = self.get(task_id)
        self.session.delete(task)
        self.session.commit()
    