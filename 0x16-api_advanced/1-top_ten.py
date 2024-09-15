#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the URL for the subreddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Get the list of posts
        posts = data['data']['children']
        
        # Print the titles of the first 10 hot posts
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        # If the subreddit is invalid, print None
        print(None)
