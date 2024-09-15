#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If the subreddit is invalid, return 0
        return 0
