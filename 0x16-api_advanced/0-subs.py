#!/usr/bin/python3
''' Module Containing Reddit API and queries'''
import requests


def number_of_subscribers(subreddit):
    ''' Queries Subreddit Api, returns the number of subscribers
            (not active users, total subscribers)
            for a given subreddit, if subreddit is invalid,
            function should return Zero(0)
    '''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        results = resp.json().get("data")
        return results.get("subscribers")
    else:
        return 0
