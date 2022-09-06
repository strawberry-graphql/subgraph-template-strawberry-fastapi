from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.post("/graphql", json={"query": "{ hello }"})
    assert response.status_code == 200
    assert response.json() == {"data": {"hello": "Hello World"}}
