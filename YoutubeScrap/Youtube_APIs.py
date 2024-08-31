#THIS  IS A TESTING BASE :IS NONE

import requests
from googleapiclient.discovery import build
import pandas as pd
#import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from IPython.display import JSON

api_key = 'AIzaSyDDIQu1ZiRt7rkzb7Ak0KAZAMW86X4udQ0'
base_url = 'https://www.googleapis.com/youtube/v3'

def search_channels(query, max_results=10):
    url = f"{base_url}/search?part=snippet&type=channel&q={query}&maxResults={max_results}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Search for Kenyan YouTube channels
kenyan_channels = search_channels("Kenya")
JSON(kenyan_channels)

print()


for item in kenyan_channels['items']:
    channel_title = item['snippet']['title']
    channel_id = item['snippet']['channelId']
    description = item['snippet']['description']

    print(f"Chanel Name: {channel_title}")
    print(f"Channel Id: {channel_id}")
    print(f"Description: {description}")
