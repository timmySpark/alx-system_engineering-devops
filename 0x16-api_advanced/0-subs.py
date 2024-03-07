#!/usr/bin/python3
''' Module Containing Reddit API and queries'''
import requests


def number_of_subscribers(subreddit):
    ''' Queries Subreddit Api, returns the number of subscribers
            (not active users, total subscribers)
            for a given subreddit, if subreddit is invalid,
            function should return Zero(0)
    '''

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_) "
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
    	try:
        	results = resp.json().get("data")
        	return results.get("subscribers")
	except Exception as e:
		return 0
    else:
        return 0
