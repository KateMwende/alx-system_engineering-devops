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
  headers = 
  response = requests.get(url, headers=headers) 
  
