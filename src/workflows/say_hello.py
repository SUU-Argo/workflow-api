from hera.workflows import Steps, Workflow, WorkflowsService, script


@script()
def echo(message: str):
    print(message)


def say_hello_workflow(name: str):
    with Workflow(
        generate_name="hello-workflow-",
        entrypoint="steps",
        workflows_service=WorkflowsService(),
    ) as w:
        with Steps(name="steps"):
            echo(arguments={"message": f"Hello {name}!"})

        w.create()

        return {"workflow_name": w.name}
