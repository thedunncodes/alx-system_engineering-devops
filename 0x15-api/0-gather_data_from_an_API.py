#!/usr/bin/python3
"""A script thatlists an employees data and completed tasks"""

from sys import argv
import json
from urllib import request

task_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
user_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'

with request.urlopen(task_url) as response:
    task_data = response.read()
with request.urlopen(user_url) as response:
    user_data = response.read()

task_data = json.loads(task_data)
user_data = json.loads(user_data)

Tasks = []


def employee_task():
    """
        This fucntion lists an employees data and completed tasks
    """

    completed_task = 0
    for user in task_data:
        if user['completed']:
            completed_task += 1
            Tasks.append(user['title'])
    print(f"Employee {user_data['name']} is done with\
            tasks({completed_task}/{len(task_data)}):")
    for task in Tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    employee_task()
