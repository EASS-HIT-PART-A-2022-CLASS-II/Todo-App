from pydantic import BaseModel
from datetime import date


class Task(BaseModel):
    task_id: int
    description: str
    creation_date: str = date.today().strftime("%d/%m/%Y")
    check = 0


def MessageResponse(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def MessageError(data,message):
    return {
        "data":data,
        "code": 404,
        "message":message,
    }