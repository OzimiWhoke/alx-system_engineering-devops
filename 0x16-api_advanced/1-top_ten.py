#!/usr/bin/python3
"""
a function that queries the Reddit API and 
prints the titles of the first 10 hot posts listed
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for i in range(min(10, len(posts))):
            title = posts[i]["data"]["title"]
            print(f"{i + 1}. {title}")
    else:
        print("None")
