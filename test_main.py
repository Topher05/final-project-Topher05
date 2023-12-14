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
	
def test_get_movie_review_full_description():
	response = client.get("/descriptions/rwe9fKfnNS0")
	assert response.status_code == 200
	assert response.json() == """CASETiFY's Bounce Cases and Clear Cases are available at casetify.com! Go to http://casetify.com/dylan today to get 15% off your order! Thanks to Casetify for sponsoring this video!

Twitter: https://twitter.com/theDMatthews
Instagram: https://www.instagram.com/neat_dylan/?hl=en"""