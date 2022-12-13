from fastapi import FastAPI, APIRouter, Body,Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.backend.models import (Task, MessageResponse, MessageError)
from typing import List

router = APIRouter()

#Connection to MongoDB
#db_connection = pymongo.MongoClient("mongodb://localhost:27017/")
#app_db = db_connection["todo_app"]
#users_col = app_db["users"]
#tasks_col = app_db["tasks"]

#------------------------ test -------------------------#

taskList = [
    Task(task_id=1,description="watch world cup final"),
    Task(task_id=2,description="watch netflix"),
    Task(task_id=3,description="run 10km"),
    Task(task_id=4,description="learn kubernetes"),
]

#Home Page
@router.get("/" , tags=["Manage Tasks"])
async def get_all_tasks():
    task = taskList
    if task:
        return MessageResponse(task,"Getting all tasks.")
    return MessageError("Error: Unable to get tasks.","Tasks not found.")


#Get task by task id
@router.get("/v1/task/{task_id}", tags=["Manage Tasks"])
async def get_task(task_id: int):
    #task = get_task_id(task_id)
    task = taskList[0]
    if task:
        return MessageResponse(task,"Task found successfully.")
    return MessageError("Error: Unable to found task.","task_id: not exists.")


#For Create a New Task
@router.post("/v1/task", tags=["Manage Tasks"])
async def create_new_task(task: Task = Body(...)):
    json = jsonable_encoder(task)
    #task = await add_task(json) #----------------------------------> Need to Create add_task in mongo database
    return MessageResponse(json,"Task created successfully.")


#For Update Existing Task
@router.put("/v1/task/{task_id}", response_model=Task, tags=["Manage Tasks"])
async def update_existing_task(task_id: int):
    #
    # need to fill
    #
    #update
    return Task


#For Delete Existing Task
@router.delete("/v1/task/{id}", tags=["Manage Tasks"])
async def delete_task(task_id: int): #-----------------------------------------> Need to Create delete_task in mongo database
    delete_task = await delete_task(task_id)
    if delete_task:
        return MessageResponse("Task ID: {} deleted successfully.".format(task_id,"Task Deleted."))
    return MessageError("Unable to delete task ID: {}".format(task_id),"Task not found or not exists.")


