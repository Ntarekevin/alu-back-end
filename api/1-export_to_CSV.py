#!/usr/bin/python3
"""
Exports all tasks owned by an employee to a CSV file using JSONPlaceholder API.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        int(employee_id)
    except ValueError:
        sys.exit(1)

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        sys.exit(1)

    user_data = user_resp.json()
    username = user_data.get("username")

    # Get todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_resp = requests.get(todos_url)
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    # Write CSV
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get
