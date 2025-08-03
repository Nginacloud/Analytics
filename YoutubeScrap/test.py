import requests
import pandas as pd

# Replace with your actual YouTube Data API key
api_key = 'AIzaSyDDIQu1ZiRt7rkzb7Ak0KAZAMW86X4udQ0'
base_url = 'https://www.googleapis.com/youtube/v3'

# Function to search for channels using keywords
def search_channels(query, max_results=10):
    url = f"{base_url}/search?part=snippet&type=channel&q={query}&maxResults={max_results}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            return data['items']
        else:
            return []
    else:
        return None

# Function to get detailed channel statistics using channel ID
def get_channel_details(channel_id):
    url = f"{base_url}/channels?part=statistics&id={channel_id}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            stats = data['items'][0]['statistics']
            return {
                "Subscribers": stats.get('subscriberCount', 'N/A'),
                "Total Videos": stats.get('videoCount', 'N/A'),
                "Total Views": stats.get('viewCount', 'N/A'),
                # Likes are not part of the Channel details, you would need to scrape video details for likes
            }
        else:
            return {
                "Subscribers": 'N/A',
                "Total Videos": 'N/A',
                "Total Views": 'N/A'
            }
    else:
        return {
            "Subscribers": 'N/A',
            "Total Videos": 'N/A',
            "Total Views": 'N/A'
        }

# Define your search queries and keywords
search_queries = ["Kenya KE", "KE", "Ke"]  # Add more keywords as needed

all_channel_data = []

# Loop over each query and perform the search
for query in search_queries:
    kenyan_channels = search_channels(query)
    
    if kenyan_channels is not None:
        for item in kenyan_channels:
            channel_title = item['snippet']['title']
            channel_id = item['snippet']['channelId']
            description = item['snippet']['description']
            
            # Fetch channel statistics
            channel_stats = get_channel_details(channel_id)
            
            # Append all data to the list
            all_channel_data.append({
                "Channel Name": channel_title,
                "Channel Id": channel_id,
                "Description": description,
                "Subscribers": channel_stats["Subscribers"],
                "Total Videos": channel_stats["Total Videos"],
                "Total Views": channel_stats["Total Views"],
                "Search Query": query  # Store the query used for the search
            })

# Convert the list to a DataFrame
df = pd.DataFrame(all_channel_data)

# Save the DataFrame to a CSV file
df.to_csv('kenyan_youtube_channels_with_stats.csv', index=False)
