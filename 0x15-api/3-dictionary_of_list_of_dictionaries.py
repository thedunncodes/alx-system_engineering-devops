#!/usr/bin/python3
"""
    This script exports data in json format
"""
import json
from urllib import request

task_url = 'https://jsonplaceholder.typicode.com/todos'
user_url = 'https://jsonplaceholder.typicode.com/users'

with request.urlopen(task_url) as response:
    task_data = response.read()
with request.urlopen(user_url) as response:
    user_data = response.read()

task_data = json.loads(task_data)
user_data = json.loads(user_data)

data = {}


def export_json():
    """
        This function reformats a json data and exports it
        into a file.
    """

    for user in user_data:
        data[f"{user['id']}"] = []
    for user in user_data:
        for task in task_data:
            if user["id"] == task["userId"]:
                data.get(f'{user["id"]}').append(
                        {"username": user['username'],
                            "task": task['title'],
                            "completed": task['completed']})

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    export_json()
