import os

from dotenv import load_dotenv
from fastapi import FastAPI
from hera.workflows import Steps, Workflow, WorkflowsService, script, Artifact
from hera.shared import global_config

load_dotenv()
global_config.host = os.getenv("ARGO_SERVER")
global_config.namespace = os.getenv("ARGO_NAMESPACE")
global_config.service_account_name = os.getenv("ARGO_SA")
app = FastAPI()

@script(outputs=Artifact(name="hello-art", path="/tmp/hello_world.txt"))
def whalesay():
    with open("/tmp/hello_world.txt", "w") as f:
        f.write("hello world")


@script(inputs=Artifact(name="message", path="/tmp/message"))
def print_message():
    with open("/tmp/message", "r") as f:
        message = f.readline()
    print(message)



@script()
def echo(message: str):
    print(message)



@app.get("/")
def read_root():
    return {"message": "Use /hello?name=yourname to start a workflow."}



@app.get("/hello")
def say_hello(name: str):
     with Workflow(
        generate_name="hello-workflow-",
        entrypoint="steps",
        workflows_service=WorkflowsService(),
    ) as w:
        with Steps(name="steps"):
            echo(arguments={"message": f"Hello {name}!"})

        w.create()

        return {"message": f"{w.to_yaml()}"}

    return w.create()


@app.get("/artifact")
def artifact():

    with Workflow(generate_name="artifact-passing-", entrypoint="artifact-example", namespace="argo", workflows_service=WorkflowsService(host="http://localhost:2746" )) as w:
        with Steps(name="artifact-example") as s:
            whalesay(name="generate-artifact")
            print_message(
                name="consume-artifact",
                arguments=[Artifact(name="message", from_="{{steps.generate-artifact.outputs.artifacts.hello-art}}")],
            )



        w.create()

        return {"message": f"{w.to_yaml()}"}
