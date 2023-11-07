#!/usr/bin/python3
"""A module for the number_of_subscribers function"""
from requests import get


def top_ten(subreddit):
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    param = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=headers, params=param, allow_redirects=False)
    try:
        data = response.json().get('data')
        for dic in data.get('children'):
            print(dic.get('data').get('title'))
    except Exception:
        print('None')
