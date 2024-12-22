import os
import mlflow

os.environ['DOCKER_HOST'] = 'unix:///Users/reece/.docker/run/docker.sock'


run_id = "e156ce6e449c4157b34a8b056911e902"
model_uri = f"runs:/{run_id}/model"

mlflow.models.build_docker(
    model_uri=model_uri,
    name="diabetes_model",
    enable_mlserver=False,
)