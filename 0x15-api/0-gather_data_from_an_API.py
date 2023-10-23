#!/usr/bin/python3
"""Python script that print information about an employee"""
import sys
import requests

if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/"
                        + user_id).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={'userId': user_id}).json()
    completed = [todo.get('title') for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task))
