#!/usr/bin/python3
''' Module Containing Reddit API and queries'''
import requests


def top_ten(subreddit):
    ''' Print titles of the first ten(10) hot posts
            listed for a given subreddit
        if subreddit not valid, print None
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
    params = {
            "limit": 10
    }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code == 404:
        print('None')
    results = resp.json().get("data")
    for data in results.get('children'):
        print(data.get('data').get('title'))
