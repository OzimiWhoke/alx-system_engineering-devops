#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, 
parses the title of all hot articles, 
and prints a sorted count of given keywords
"""
import requests

def count_words(subreddit, word_list, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            words = title.split()

            for word in words:
                # Check if the word is in the word_list and is not a variant like java. or java!
                if word in word_list and word[-1].isalpha():
                    counts[word] = counts.get(word, 0) + 1

        after = data["data"]["after"]
        if after is not None:
            return count_words(subreddit, word_list, counts=counts, after=after)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None
