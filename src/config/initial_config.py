import os

from dotenv import load_dotenv
from hera.shared import global_config


def load_env():
    load_dotenv()
    global_config.host = os.getenv("ARGO_SERVER")
    global_config.namespace = os.getenv("ARGO_NAMESPACE")
    global_config.service_account_name = os.getenv("ARGO_SA")
