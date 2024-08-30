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


def fetch_youtube_data(youtube, channel_ids):
    
    # Fetch channel details
    channel_data = get_channel_details(youtube, channel_ids)
    
    # Initialize a list to collect video details DataFrames
    all_video_info = []

    # Loop through each channel to get video details
    for idx, row in channel_data.iterrows():
        playlist_id = row['playlistId']
        video_ids = get_video_ids(youtube, playlist_id)
        video_info_data = get_video_details(youtube, video_ids)
        all_video_info.append(video_info_data)

    
    video_info_data_combined = pd.concat(all_video_info, ignore_index=True)

    # Merge channel data with combined video details
    final_data = pd.merge(video_info_data_combined, channel_data, left_on='channelTitle', right_on='channelName', how='left')


    print(final_data)
    final_data.to_csv('kenyan_youtube_data1.csv', index=False)

    # Return the final DataFrame for further use if needed
    return final_data


