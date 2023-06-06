#!/usr/bin/python3
""" 
a function that queries the Reddit API 
and returns the number of subscribers 
"""

import requests

def number_of_subscribers(subreddit):

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
