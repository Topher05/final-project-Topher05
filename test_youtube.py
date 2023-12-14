from fastapi.testclient import TestClient
from youtube import Youtube

def test_movie_review_search():
	search_response = Youtube.movie_review_search('Cars')
	assert "cars" in search_response[0]["title"].lower()
	