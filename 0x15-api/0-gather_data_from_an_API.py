#!/usr/bin/env python3
"""this is to get employee is information"""


from nturl2path import url2pathname
from sys import argv
import requests


if __name__ == '__main__':
    count = 0
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    info = requests.get(url1).json()
    todo = requests.get(url2).json()
    emp_name = info.get('name')
    task_title = []
    for row in todo:
        if row.get('completed') is True:
            count += 1
            task_title.append(row.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name,
        count,
        len(todo)
        ))
    for title in task_title:
        print("\t {}".format(title))
