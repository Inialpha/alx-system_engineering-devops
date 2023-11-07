#!/usr/bin/python3
"""A module for the number_of_subscribers function"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    param = {'limit': 100, 'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=headers, params=param, allow_redirects=False)
    try:
        after = response.json().get('data').get('after')
        if after:
            recurse(subreddit, hot_list, after)
        data = response.json().get('data').get('children')
        for dic in data:
            hot_list.append(dic.get('data').get('title'))
        return hot_list
    except Exception:
        return None
