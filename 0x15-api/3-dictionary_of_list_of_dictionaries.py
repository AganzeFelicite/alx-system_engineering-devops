#!/usr/bin/python3
"""this is to get employee is information"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    url1 = "https://jsonplaceholder.typicode.com/users/"
    url2 = "https://jsonplaceholder.typicode.com/todos"
    info = requests.get(url1).json()
    todo = requests.get(url2).json()
    data = []
    my_dict = {}
    for item in info:
        data = []
        for row in todo:
            if item.get('id') == row.get('userId'):
                a_row = ({
                    "username": item.get('name'),
                    "task": row.get('title'),
                    "completed": row.get('completed')
                    })
                data.append(a_row)
            my_dict[row.get('userId')] = data
    with open('todo_all_employees.json', 'w') as new_file:
        json.dump(my_dict, new_file)
