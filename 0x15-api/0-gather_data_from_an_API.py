#!/usr/bin/python3
"""Accessinh a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    num = int(sys.argv[1])

    n = requests.get('https://jsonplaceholder.typicode.com/users')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    
    r_list = r.json()
    n_list = n.json()
    
    completed_tasks = 0
    max_task = 0
    name = ""
    
    for i in n_list:
        if i['id'] == num:
            name = i['name']

    for i in r_list:
        if i['userId'] == num:
            max_task += 1

    for i in r_list:
        if i['userId'] == num and i['completed'] == True:
            completed_tasks += 1

    print(f'Employee {name} is done with tasks({completed_tasks}/{max_task}):')
    for i in r_list:
        if i['userId'] == num and i['completed'] == True:
            print('\t', i['title'])
