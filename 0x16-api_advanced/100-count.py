#!/usr/bin/python3
"""count words"""
from requests import get


def count_words(subreddit, word_list):
    """count words"""
    count = {}
    retrieve_word_counts(subreddit, word_list, count)
    print(count)


def retrieve_word_counts(subreddit, word_list, count={}, after=None):
    """count words"""
    head = {'User-Agent': 'Mozilla/5.0'}
    param = {'limit': 100, 'after': after} if after else {'limit': 100}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    try:
        response = get(url, headers=head, params=param, allow_redirects=False)

        if response.status_code != 200:
            return

        after = response.json().get('data').get('after')

        if after:
            retrieve_word_counts(subreddit, word_list, count, after)

        data = response.json().get('data').get('children')

        for dic in data:
            title = dic.get('data').get('title')
            for word in word_list:
                for t in title.split():
                    if t.lower() == word.lower():
                        count[word.lower()] = count.get(word.lower(), 0) + 1

    except Exception as e:
        return
