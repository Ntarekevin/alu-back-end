#!/usr/bin/python3
"""
Script that fetches and displays the TODO list progress of an employee
based on their ID using JSONPlaceholder API.
"""

import requests
import sys

if __name__ == "__main__":
    # Validate argument count
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        int_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Define base URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Process TODOs
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    num_done_tasks = len(done_tasks)

    # Output
    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
