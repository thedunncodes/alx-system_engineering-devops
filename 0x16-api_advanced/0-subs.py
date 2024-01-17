#!/usr/bin/python3
'''
A script to query reddit api
'''

import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
    Returns number of subscribers in a subreddit
    '''

    header = {"user_agent": "Alx_api"}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()
        print(data.get('data').get('subscribers'))
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
