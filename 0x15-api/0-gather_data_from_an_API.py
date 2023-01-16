#!/usr/bin/python3

import requests
import sys

num = int(sys.argv[1])


def get_todo(num):
    """
    Retrieves information about an employee TODO list

    param1: n - requests for employee users json
    param2: r - requests for all employee tasks json
    param3: num - retrieves input from the commandline
    """
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
            print(i['title'])


get_todo(num)
