#!/usr/bin/python3
"""Exports employee task data to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    username = user.get("username")

    # Get todos
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").json()

    # Write to CSV
    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
