#!/usr/bin/python3
'''
A script thatlists an employees data and completed tasks
'''

import json
from sys import argv
from urllib import request

if __name__ == '__main__':
    if len(argv) > 1:
        task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
                        .format(argv[1])
        user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
            .format(argv[1])
        with request.urlopen(task_url) as response:
            task_data = response.read()
        with request.urlopen(user_url) as response:
            user_data = response.read()

        task_data = json.loads(task_data)
        user_data = json.loads(user_data)

        Tasks = []

        def employee_task():
            '''
                This fucntion lists an employees data and completed tasks
            '''

            completed_task = 0
            for user in task_data:
                if user['completed']:
                    completed_task += 1
                    Tasks.append(user['title'])
            print("Employee {} is done with tasks({}/{}):"
                  .format(user_data['name'], completed_task, len(task_data)))
            for task in Tasks:
                print(f"\t {task}")

    employee_task()
