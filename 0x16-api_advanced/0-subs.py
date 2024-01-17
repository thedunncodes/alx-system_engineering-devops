#!/usr/bin/python3
""" module to query reddit """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Queries reddit for:
        Number of subscribers"""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
