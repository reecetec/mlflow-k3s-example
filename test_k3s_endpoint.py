import json

import requests
from sklearn.datasets import load_diabetes


def main():
    diabetes = load_diabetes()

    test_sample = diabetes.data[0:1]

    def predict(data):
        response = requests.post(
            "http://localhost:30000/invocations",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"inputs": data}),
            timeout=5,
        )
        return response.json()

    result = predict(test_sample.tolist())
    print(result)


if __name__ == "__main__":
    main()
