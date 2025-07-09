#!/usr/bin/python3
"""This module gathers data from an API and displays employee's completed tasks"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Fetch todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(todos_url).json()

    # Get completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    # Print result
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
