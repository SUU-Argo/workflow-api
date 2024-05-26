## workflow-api

### Local setup

1. Some kind of k8s cluster (e.g. [minikube](https://minikube.sigs.k8s.io/docs/start/)) with
   [argo](https://argo-workflows.readthedocs.io/en/latest/quick-start/) installed is required.

2. Install project dependencies with poetry:

```bash
poetry shell
poetry install
```

3. Run the FastAPI server:

```bash
uvicorn src.main:app --reload
```
