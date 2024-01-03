from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from db import CRUD
from typing import Optional

app = FastAPI(
    title="Simple task API",
    description=" A simple API built using AppWrite's db",
    docs_url="/"
)

crud = CRUD()


class TaskCreateModel(BaseModel):
    name: str
    description: Optional[str] = None  # Make description optional
    date_added: Optional[str] = Field(default=datetime.utcnow().isoformat())
    due_date: str
    completed: Optional[bool] = None  # Make completed optional


class TaskUpdateModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None  # Make description optional
    due_date: Optional[str] = None
    completed: Optional[bool] = None 


@app.get('/tasks')
async def get_all_tasks():
    result = crud.list_tasks()

    return result


@app.get('/task/{task_id}')
async def get_task(task_id: str):
    result = crud.retrieve_task(task_id)

    return result


@app.post('/tasks', status_code=201)
async def create_task(task_data: TaskCreateModel):
    result = crud.create_task(data={
        'name': task_data.name,
        'description': task_data.description,
        'due_date' : task_data.due_date,
        'date_added': task_data.date_added,
        'completed': task_data.completed
    })

    return result


@app.patch('/task/{task_id}')
async def Update_task(task_id: str, update_data: TaskUpdateModel):
    update_dict = update_data.dict(exclude_unset=True)
    result = crud.update_task(
        task_id=task_id,
        data=update_dict
    )

    return result


@app.delete('/task/{task_id}', status_code=204)
async def get_all_tasks(task_id: str):
    result = crud.delete_task(
        task_id=task_id
    )

    return result
