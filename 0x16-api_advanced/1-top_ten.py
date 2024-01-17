#!/usr/bin/python3
'''
A script to query reddit api
'''

import requests
from sys import argv


def top_ten(subreddit):
    '''
    Returns number of subscribers in a subreddit
    '''

    header = {"user_agent": "Alx_api/1.0"}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for dt in data:
            print(dt.get('data').get('title'))
    else:
        return 0


if __name__ == "__main__":
    top_ten(argv[1])
