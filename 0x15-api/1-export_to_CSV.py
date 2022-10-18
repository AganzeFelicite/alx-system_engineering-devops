#!/usr/bin/python3
"""this is to get employee is information"""


import csv
import requests
from sys import argv


if __name__ == '__main__':
    count = 0
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    info = requests.get(url1).json()
    todo = requests.get(url2).json()
    e_name = info.get('username')
    with open('{}.csv'.format(argv[1]), 'w') as new_file:
        data = csv.writer(new_file, quoting=csv.QUOTE_ALL)
        for row in todo:
            item = [
                row.get('userId'),
                e_name, row.get('completed'),
                row.get('title')
                ]
            data.writerow(item)
