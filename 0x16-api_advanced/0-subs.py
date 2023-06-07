#!/usr/bin/python3
"""
Returns number of subscribers from Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Checks number of sucribers in a subreddit
    """
    url = 'https://www.reddit.com/r/{}.about.json.format(subreddit)'
    headers = {'User-Agent': 'linux:countSubs:v0.01(by /u/cmm_94)'}
    response = requests.get(url, headers=headers)

    data = response.json().get('data')
    count = data.get("subscribers")

    if response.status_code == 200:
        return (count)
    else:
        return (0)
