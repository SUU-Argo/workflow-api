import os

from dotenv import load_dotenv
from fastapi import FastAPI
from hera.shared import global_config
from hera.workflows import Steps, Workflow, WorkflowsService, script

load_dotenv()
global_config.host = os.getenv("ARGO_SERVER")
global_config.namespace = os.getenv("ARGO_NAMESPACE")
global_config.service_account_name = os.getenv("ARGO_SA")
app = FastAPI()


@script()
def echo(message: str):
    print(message)


@app.get("/hello")
def read_root(message: str = "Hello World!"):
    with Workflow(
        generate_name="hello-world-",
        entrypoint="steps",
        workflows_service=WorkflowsService(),
    ) as w:
        with Steps(name="steps"):
            echo(arguments={"message": message})

    return w.create()
