from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from db import CRUD

app = FastAPI(
    title="Simple task API",
    description=" A simple API built using AppWrite's db",
    docs_url="/"
)

crud = CRUD()


class TaskCreateModel(BaseModel):
    name: str
    description: str
    date_added: str = Field(default=datetime.utcnow().isoformat())
    due_date: str


class TaskUpdateModel(BaseModel):
    name: str
    description: str
    due_date: str


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
        'date_added': task_data.date_added
    })

    return result


@app.patch('/task/{task_id}')
async def Update_task(task_id: str, update_data: TaskUpdateModel):
    result = crud.update_task(
        task_id=task_id,
        data={
            'name': update_data.name,
            'description': update_data.description,
            'due_date' : task_data.due_date,
        }
    )

    return result


@app.delete('/task/{task_id}', status_code=204)
async def get_all_tasks(task_id: str):
    result = crud.delete_task(
        task_id=task_id
    )

    return result
