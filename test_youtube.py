from fastapi.testclient import TestClient
from youtube import Youtube

def test_movie_review_search():
	search_response = Youtube.movie_review_search('Cars')
	assert "cars" in search_response[0]["title"].lower()

def test_movie_review_full_description():
	list_response = Youtube.movie_review_full_description('rwe9fKfnNS0')
	assert list_response == """CASETiFY's Bounce Cases and Clear Cases are available at casetify.com! Go to http://casetify.com/dylan today to get 15% off your order! Thanks to Casetify for sponsoring this video!

Twitter: https://twitter.com/theDMatthews
Instagram: https://www.instagram.com/neat_dylan/?hl=en"""

def test_movie_review_diff_langauge():
	new_lang_response = Youtube.movie_review_diff_langauge('Cars', "zh-Hans")
	assert "汽车" in new_lang_response[0]["title"]
	