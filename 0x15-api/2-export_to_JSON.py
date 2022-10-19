#!/usr/bin/python3
"""this is to get employee is information"""


from ast import arg
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
                    "task": row.get('title'),
                    "completed": row.get('completed'),
                    "username": info.get('username'),
                    })
    my_dict = {argv[1]: data}
    with open('{}.json'.format(argv[1]), 'w') as new_file:
        json.dump(my_dict, new_file)
