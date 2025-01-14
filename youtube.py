import sys 
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class Youtube:
	def movie_review_search(qterm):
		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
								developerKey=DEVELOPER_KEY)

		search_response = youtube.search().list(
			q=qterm + 'movie review/commentary',
			part='id,snippet',
			maxResults=10,
		).execute()

		movieList = []
		for m in search_response.get('items', []):
			movieList.append(dict(id = m['id']['videoId'], title = m['snippet']['title'], description = m['snippet']['description']))

		return movieList
	
	def movie_review_full_description(videoId):
		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
								developerKey=DEVELOPER_KEY)
		list_response = youtube.videos().list(
			id=videoId,
			part='snippet'
		).execute()
		return list_response['items'][0]['snippet']['description']
	
	def movie_review_diff_langauge(qterm, language):
		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
								developerKey=DEVELOPER_KEY)
		
		service = build(
        "translate", "v2", developerKey="AIzaSyASAGC6fpVUFxROHLQN-DcLkIhjBDkuBM0")
    	
		translation = service.translations().list(source="en", target=language, q=[qterm+'movie review/commentary']).execute()
		#print(translation['translations'][0]['translatedText'])

		search_response = youtube.search().list(
			q=translation['translations'][0]['translatedText'],
			part='id,snippet',
			maxResults=10,
		).execute()

		movieList = []
		for m in search_response.get('items', []):
			movieList.append(dict(id = m['id']['videoId'], title = m['snippet']['title'], description = m['snippet']['description']))

		return movieList
	


#print(Youtube.movie_review_full_description('rwe9fKfnNS0'))
# movieName = input("Enter movie name:")
# try:
# 	print(Youtube.movie_review_search(movieName))
# except HttpError as e:
# 		print('An HTTP error %d occurred:\n%s' % (type(e).__name__, str(e)))

# try:
# 	print(Youtube.movie_review_diff_langauge("cars", "zh-Hans"))
# except HttpError as e:
# 		print('An HTTP error %d occurred:\n%s' % (type(e).__name__, str(e)))