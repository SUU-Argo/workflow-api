from fastapi import APIRouter

from .workflows.artifact import artifact_workflow
from .workflows.say_hello import say_hello_workflow
from .workflows.mapreduce import map_reduce_workflow

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Use /hello?name=yourname to start a workflow."}


@router.get("/hello")
def say_hello(name: str):
    return say_hello_workflow(name)


@router.get("/artifact")
def artifact():
    return artifact_workflow()


@router.get("/map")
def map(workers: int, text: str):
    return map_reduce_workflow(workers,text)
