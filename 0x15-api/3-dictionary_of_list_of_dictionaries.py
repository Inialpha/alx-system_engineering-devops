#!/usr/bin/python3
"""Python script that print information about an employee"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    dic = {}
    for user in users:
        user_dic = []
        todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                             params={'userId': user.get('id')}).json()
        for task in todos:
            user_dic.append({
                             'username': user.get('username'),
                             'task': task.get('title'),
                             'completed': task.get('completed')})
        dic[user.get('id')] = user_dic
    with open("todo_all_employees.json", 'w') as f:
        json.dump(dic, f)
