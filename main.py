from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Task(BaseModel):
    id: int
    text: str
    state: str
    
@app.get("/")
def read():
    json_load = []
    if os.path.isfile('todo.json'):
        with open('todo.json', 'r') as json_file:
            json_load = json.load(json_file)
    else:
        raise Exception("todo.json not found")

    return json_load

@app.post("/")
def create(task: Task):
    json_load = []
    task_dict = task.dict()

    if os.path.isfile('todo.json'):
        with open('todo.json', 'r') as json_file:
            json_load = json.load(json_file)
    else:
        raise Exception("todo.json not found")
    
    json_load.insert(0,task_dict)

    with open('todo.json', 'w') as json_file:
            json.dump(json_load,json_file)

    return json_load


@app.put("/{new_task_id}")
def update(new_task_id:int, new_task:Task):

    json_load = []
    new_task_dict = new_task.dict()
    
    if os.path.isfile('todo.json'):
        with open('todo.json', 'r') as json_file:
            json_load = json.load(json_file)
    else:
        raise Exception("todo.json not found")
    
    for index, task in enumerate(json_load):
        if task["id"] == new_task_id:
            json_load[index] = new_task_dict
    
    with open('todo.json', 'w') as json_file:
        json.dump(json_load, json_file)
             
    return json_load


@app.delete("/")
def delete(task:Task):

    json_load = []
    task_dict = task.dict()
    
    if os.path.isfile('todo.json'):
        with open('todo.json', 'r') as json_file:
            json_load = json.load(json_file)
    else:
        raise Exception("todo.json not found")
    
    json_load.remove(task)

    with open('todo.json', 'w') as json_file:
        json.dump(json_load, json_file)
    
    return json_load