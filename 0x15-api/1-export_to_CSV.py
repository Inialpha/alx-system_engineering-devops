#!/usr/bin/python3
"""get user info to csv file"""

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/"
                        + user_id).json()

    username = user.get("username")
    filename = user_id + '.csv'
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get('completed'),
                            task.get('title')])
