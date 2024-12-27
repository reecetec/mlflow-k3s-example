#!/bin/bash

docker run --rm -p 8080:8080 diabetes_model > /dev/null 2>&1 &
sleep 5

uv run test_endpoint.py

docker ps -q --filter ancestor=diabetes_model | xargs -r docker stop 2>&1