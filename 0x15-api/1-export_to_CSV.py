#!/usr/bin/python3
'''
This script exports data in csv format
'''

import csv
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

        data = []

        def export_json():
            '''
                This function reformats a json data and exports it
                into a csv file.
            '''

            for user in task_data:
                data.append(['\"{}\"'.format(argv[1]),
                             '\"{}\"'.format(user_data['username']),
                             '\"{}\"'.format(user['completed']),
                             '\"{}\"'.format(user['title'])])

            for user in data:
                print(user)

            with open('{}.csv'.format(argv[1]), 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)

    export_json()
