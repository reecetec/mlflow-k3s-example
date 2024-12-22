import requests
import numpy as np
from sklearn.datasets import load_diabetes
import json

def test_model_endpoint():

    # after running docker run -p 8080:8080 diabetes_model

    diabetes = load_diabetes()
     
    test_sample = diabetes.data[0:1]  
    
    inference_request = {
        "inputs": test_sample.tolist()
    }
    
    try:
        response = requests.post(
            "http://localhost:8080/invocations",
            json=inference_request,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            prediction = response.json()
            print("\nPrediction successful!")
            print(f"Input features: {test_sample[0]}")
            print(f"Predicted value: {prediction}")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response content: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the model server. Is the container running?")

if __name__ == "__main__":
    test_model_endpoint()