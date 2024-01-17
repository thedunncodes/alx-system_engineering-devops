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

    header = {'user_agent': 'Alx_api'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        print(data.get('data').get('subscribers'))
    else:
        return (0)
