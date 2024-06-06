from pydantic import BaseModel


class MapReduceRequest(BaseModel):
    workers: int
    text: str
