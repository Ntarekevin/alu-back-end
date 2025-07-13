#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user information
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch tasks for the user
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Export to CSV
    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get('completed'), task.get('title')])
