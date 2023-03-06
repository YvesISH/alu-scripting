#!/usr/bin/python3
"""Return number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """The funct"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code = 200:
        json_data = response.json()
        subscriber_number = json_dataget('data').get(
            'children')[0].get('data').get('subreddit_subscribers')
        return subscriber_number
    else:
        return 0
