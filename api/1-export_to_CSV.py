#!/usr/bin/python3
"""Exports user's TODO list data to a CSV file"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f'{base_url}/users/{user_id}'
    todos_url = f'{base_url}/todos?userId={user_id}'

    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)

    if user_resp.status_code != 200 or todos_resp.status_code != 200:
        sys.exit(1)

    user_data = user_resp.json()
    username = user_data.get('username')
    todos = todos_resp.json()

    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                str(task.get('completed')),
                task.get('title')
            ])