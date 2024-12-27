#!/bin/bash

if [ -z "$1" ]; then
   echo "Usage: $0 <model_run_uri>/<path_to_model_folder_from_artifacts>"
   echo "Example: $0 e156ce6e449c4157b34a8b056911e902/model"
   exit 1
fi

mlflow models generate-dockerfile -m "runs:/$1" -d "mlflow-dockerfile"
docker build -t diabetes_model mlflow-dockerfile/.