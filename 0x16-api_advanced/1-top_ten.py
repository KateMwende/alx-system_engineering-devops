#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    First 10 hot posts in the subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'topTen/0.0.1(by /u/cmm_94)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        posts = response.json().get("data").get("children")

        if response.status_code == 200:
            for post in posts:
                print(post.get('data').get('title'))
    except Exception:
        print(None)
