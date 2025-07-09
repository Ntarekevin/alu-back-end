#!/usr/bin/python3
"""Exports employee task data to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(user_url).json()
    username = user.get("username")

    # Get user todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(todos_url).json()

    # Create CSV file
    file_name = f"{user_id}.csv"
    with open(file_name, mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
init