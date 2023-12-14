from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_helloworld(): 
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {
		"Hello": "World"
		}

def test_get_movie_reviews():
	response = client.get("/moviereviews/cars")
	assert response.status_code == 200
	assert "cars" in response.json()[0]["title"].lower() 