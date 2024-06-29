#!/usr/bin/python3
"""
Get to-do progress of an employee
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    try:
        user_info = requests.get(user_url).json()
        todos_info = requests.get(todos_url).json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    employee_name = user_info.get("name")
    if not employee_name:
        print("Employee not found.")
        sys.exit(1)

    task_completed = [task for task in todos_info if task.get("completed") is True]
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, number_of_done_tasks, total_number_of_tasks))

    for task in task_completed:
        print("\t {}".format(task.get("title")))
