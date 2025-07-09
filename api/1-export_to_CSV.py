#!/usr/bin/python3
"""Exports employee task data to CSV format."""

import csv
import requests
import sys

def fetch_user_info(user_id):
    """Fetch user information from the API."""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    response.raise_for_status()
    return response.json()

def fetch_user_todos(user_id):
    """Fetch user todos from the API."""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos",
        params={"userId": user_id}
    )
    response.raise_for_status()
    return response.json()

def write_to_csv(user_id, username, todos):
    """Write user task data to a CSV file."""
    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        try:
            user = fetch_user_info(user_id)
            username = user.get("username")
            todos = fetch_user_todos(user_id)
            write_to_csv(user_id, username, todos)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python script.py <user_id>")
        