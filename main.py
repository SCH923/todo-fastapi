from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

class Task(BaseModel):
    text: str
    done: bool
    
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


@app.put("/")
def update():
    return {"message": "Hello World"}


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