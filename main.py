from fastapi import FastAPI
from youtube import Youtube

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/moviereviews/{movie_name}")
def get_movie_reviews(movie_name):
    return Youtube.movie_review_search(movie_name)

@app.get("/descriptions/{video_id}")
def get_movie_review_full_description(video_id):
    return Youtube.movie_review_full_description(video_id)