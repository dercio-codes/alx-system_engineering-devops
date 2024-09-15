#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Define the URL for the subreddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Define parameters for pagination
    params = {
        'limit': 100,  # Maximum number of posts to return
        'after': after  # Pagination token
    }
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data['data']['children']
        
        # Append titles to the hot_list
        hot_list.extend([post['data']['title'] for post in posts])
        
        # Get the 'after' token for pagination
        after = data['data']['after']
        
        # If there are more posts to fetch, call recurse again
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # If the subreddit is invalid, return None
        return None

# Example usage:
if __name__ == '__main__':
    subreddit_name = 'programming'  # Example subreddit
    titles = recurse(subreddit_name)
    if titles is not None:
        for title in titles:
            print(title)
    else:
        print("None")
