#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all
    hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'topArticles/0.0.1(by /u/cmm_94)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        after = response.json().get('data').get('after')
        posts = response.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
