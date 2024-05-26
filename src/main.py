from fastapi import FastAPI
import couler.argo as couler
from couler.argo_submitter import ArgoSubmitter

app = FastAPI()


@app.get("/")
def read_root():
    couler.run_container(
        image="docker/whalesay", command=["cowsay"], args=["hello world"]
    )

    submitter = ArgoSubmitter()
    result = couler.run(submitter=submitter)
    return {"message": result}
