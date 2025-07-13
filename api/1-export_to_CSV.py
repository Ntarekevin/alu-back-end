#!/usr/bin/python3
"""
Exports employee TODO list data to CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    username = user_response.json().get("username")

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    tasks = todos_response.json()

    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")])
