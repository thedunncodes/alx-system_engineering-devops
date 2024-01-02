#!/usr/bin/python3
'''
This script exports data in json format
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

        data = {f"{argv[1]}": []}

        def export_json():
            '''
                This function reformats a json data and exports it
                into a file.
            '''

            for user in task_data:
                data.get(f'{argv[1]}').append(
                                    {"task": user['title'],
                                        "completed": user['completed'],
                                        "username": user_data['username']})

            with open('{}.json'.format(argv[1]), 'w') as json_file:
                json.dump(data, json_file)

    export_json()
