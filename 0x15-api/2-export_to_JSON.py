#!/usr/bin/python3
"""Python script that print information about an employee"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/"
                        + user_id).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={'userId': user_id}).json()
    completed = [todo.get('title') for todo in todos if todo.get("completed")]
    dic = {user_id: [{
                      'task': task.get('title'),
                      'completed': task.get('completed'),
                      'username': user.get('username')} for task in todos]}
    filename = user_id + ".json"
    with open(filename, 'w') as f:
        json.dump(dic, f)
