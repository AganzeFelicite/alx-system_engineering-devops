#!/usr/bin/python3
"""this is to get employee is information"""


import json
from html2text import element_style
import requests
from sys import argv


if __name__ == '__main__':
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    info = requests.get(url1).json()
    todo = requests.get(url2).json()
    data = []
    for row in todo:
        data.append({
            row.get('userId'): [
                {
                    "task": row.get('title'),
                    "completed": row.get('completed'),
                    "username": info.get('username')
                }
            ]
        })
    with open('{}.json'.format(argv[1]), 'w') as new_file:
        json.dump(data, new_file, indent=4)
