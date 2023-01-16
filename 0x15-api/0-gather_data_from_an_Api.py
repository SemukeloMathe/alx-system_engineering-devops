#!/usr/bin/python3

"""A Python script that uses REST API for a given employee and
returns information his/her TODO list progress"""

import requests
import sys

"""Here we are getting the employees information"""
n = requests.get('https://jsonplaceholder.typicode.com/users')

"""Here we are accesing the users tasks"""
r = requests.get('https://jsonplaceholder.typicode.com/todos')

"""Now we store the json info received in a lists"""
r_list = r.json()
n_list = n.json()

"""Here we getting the input from the commandline"""
num = int(sys.argv[1])
completed_tasks = 0
total_tasks = 0
name = ""

"""for loop for iterating through the employee list to retrieve a name"""
for i in n_list:
    if i['id'] == num:
        name = i['name']

"""for loop for retrieving total tasks """
for i in r_list:
    if i['userId'] == num:
        total_tasks += 1

"""for loop for retrieving completed tasks"""
for i in r_list:
    if i['userId'] == num and i['completed'] == True:
        completed_tasks += 1

print(f'Employee {name} is done with tasks({completed_tasks}/{total_tasks}):')
for i in r_list:
    if i['userId'] == num and i['completed'] == True:
        print(i['title'])
