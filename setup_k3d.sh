k3d cluster create mlflow-cluster --port '30000:30000@loadbalancer'

k3d image import diabetes_model -c mlflow-cluster

kubectl apply -f k8s/model-deploy.yaml