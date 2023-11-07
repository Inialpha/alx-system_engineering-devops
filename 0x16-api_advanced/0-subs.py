#!/usr/bin/python3
"""A module for the number_of_subscribers function"""
from requests import get


def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    response = get(url, headers=headers)
    data = response.json().get('data')
    try:
        return data.get('subscribers')
    except Exception:
        return 0
