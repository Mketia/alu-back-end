#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    try:
        # Fetch employee details
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch employee's TODO list
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        todo_response.raise_for_status()
        todos = todo_response.json()

        # Calculate TODO progress
        total_tasks = len(todos)
        done_tasks = [task for task in todos if task['completed']]
        number_of_done_tasks = len(done_tasks)

        # Print the result
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
