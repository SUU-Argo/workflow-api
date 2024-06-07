from fastapi import APIRouter

from .requests.map_reduce import MapReduceRequest
from .workflows.artifact import artifact_workflow
from .workflows.map_reduce import map_reduce_workflow
from .workflows.say_hello import say_hello_workflow

router = APIRouter()


@router.get("/")
def read_root():
    return {
        "available_workflows": [
            {"method": "GET", "path": "/hello"},
            {"method": "GET", "path": "/artifact"},
            {"method": "POST", "path": "/map-reduce"},
        ]
    }


@router.get("/hello")
def say_hello(name: str):
    return say_hello_workflow(name)


@router.get("/artifact")
def artifact():
    return artifact_workflow()


@router.post("/map-reduce")
def map_reduce(map_reduce_request: MapReduceRequest):
    return map_reduce_workflow(map_reduce_request.workers, map_reduce_request.text)
