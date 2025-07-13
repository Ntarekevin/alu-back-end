#!/usr/bin/python3

import json

def check_users_and_tasks(file_path):
    # Load data from the JSON file
    with open(file_path, 'r') as file:
        employees_tasks = json.load(file)

    # Define expected user IDs
    expected_user_ids = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}

    # Check if all expected user IDs are present
    found_user_ids = set(employees_tasks.keys())

    if found_user_ids != expected_user_ids:
        print(f"Users found incorrect. Missing or extra users: {found_user_ids.symmetric_difference(expected_user_ids)}")
        return

    # Check if all users have tasks
    all_correct = True
    for user_id in expected_user_ids:
        if not employees_tasks[user_id]:
            print(f"User ID {user_id} Tasks: Incorrect or not found")
            all_correct = False

    if all_correct:
        print("All users found: OK")
        print("User ID and Tasks output: OK")
    else:
        print("Some user IDs or tasks are incorrect or missing.")

# Path to your JSON file
file_path = 'todo_all_employees.json'

# Run the check
check_users_and_tasks(file_path)
