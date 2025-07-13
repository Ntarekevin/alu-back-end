#!/usr/bin/python3
"""
This script handles exporting tasks for a given employee ID to a JSON file,
checking the user ID, and verifying the structure and presence of tasks.
"""

import json
import requests
import sys

def export_to_json(employee_id):
    """
    Export tasks for a given employee ID to a JSON file.

    Parameters:
    employee_id (int): The ID of the employee whose tasks are to be exported.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    username = user_response.json().get("username")
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    tasks = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    } for task in todos]

    output_data = {str(employee_id): tasks}
    filename = f"{employee_id}.json"

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(output_data, jsonfile)

    print(f"Data has been exported to {filename}")

def check_user_id(employee_id):
    """
    Check if the provided user ID is correct by querying an API.

    Parameters:
    employee_id (int): The ID of the employee to check.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code == 200:
        print("Correct USER_ID: OK")
        return True
    else:
        print("User not found")
        return False

def check_user_tasks(employee_id):
    """
    Check if the user ID's value is a list of dictionaries.

    Parameters:
    employee_id (int): The ID of the employee to check.
    """
    filename = f"{employee_id}.json"

    try:
        with open(filename, mode="r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        if isinstance(data.get(str(employee_id)), list):
            if all(isinstance(task, dict) for task in data.get(str(employee_id), [])):
                print("USER_ID's value type is a list of dicts: OK")
            else:
                print("USER_ID's value type is not a list of dicts")
        else:
            print("USER_ID's value type is not a list of dicts")
    except FileNotFoundError:
        print(f"File {filename} not found")
        sys.exit(1)

def check_all_tasks(employee_id):
    """
    Check if all tasks are found in the list of dictionaries.

    Parameters:
    employee_id (int): The ID of the employee to check.
    """
    filename = f"{employee_id}.json"

    try:
        with open(filename, mode="r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        tasks = data.get(str(employee_id), [])
        if tasks:
            print("All tasks found: OK")
        else:
            print("No tasks found")
    except FileNotFoundError:
        print(f"File {filename} not found")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    if check_user_id(employee_id):
        export_to_json(employee_id)
        check_user_tasks(employee_id)
        check_all_tasks(employee_id)
