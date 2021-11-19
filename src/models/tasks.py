from datetime import date

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    text: str
    date: date

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    is_done: bool