## workflow-api

### Local setup

1. Some kind of k8s cluster (e.g. [kind](https://kind.sigs.k8s.io/docs/user/quick-start)), 
   [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) and 
   [argo](https://argo-workflows.readthedocs.io/en/latest/quick-start/) is required.
2. Disable authentication and HTTPS for argo (it's not necessary but very helpful for local development):
   ```bash
   kubectl patch deployment \
     argo-server \
     --namespace argo \
     --type='json' \
     -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/args", "value": [
     "server",
     "--auth-mode=server",
     "--secure=false",
     "--access-control-allow-origin=*",
   ]},
   {"op": "replace", "path": "/spec/template/spec/containers/0/readinessProbe/httpGet/scheme", "value": "HTTP"}
   ]'
   ```
3. You can port-forward argo UI:
   ```bash
   kubectl -n argo port-forward --address 0.0.0.0 svc/argo-server -n argo 2746:2746
   ```
   UI will be available at http://localhost:2746
4. Create cluster role, service account and cluster role binding for argo:
   ```bash
   kubectl apply -f deploy/02-workflow-api-svcaccount.yaml
   ```
5. Install project dependencies with poetry:
   ```bash
   poetry shell
   poetry install
   ```
6. Run the FastAPI server:
   ```bash
   uvicorn src.main:app --reload
   ```
