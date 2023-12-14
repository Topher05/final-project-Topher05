# final-project-Topher05

Steps to running the program:

	-Clone or download the files
	-Create a vertual environment in the folder with the files (something like python3 -m venv .venv)
	-Activate the virtual environment and install the required methods with pip install -r requirements.txt
	-Then all you need to do is run uvicorn main:app --reload and the app should start 
	-Exit by pressing control c in the terminal
	-To run test just use the command pytest in the terminal
	-navigating to /moviereviews/{movie_name} and /descriptions/{video_id}
	 where {movie_name} equals the movie you want to search and 
	 {video_id} equals the video id you want the description of
	 -alternatively you can go to /docs which will let you see all the methods
