#!/usr/bin/python3
"""
Checks if the provided user ID is correct and outputs a confirmation message.
"""

import json
import requests
import sys

def check_user_id(employee_id):
    """
    Check if the provided user ID is correct by querying an API.

    Parameters:
    employee_id (int): The ID of the employee to check.

    Returns:
    bool: True if the user ID is correct, False otherwise.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code == 200:
        print("Correct USER_ID: OK")
        return True
    else:
        print("User not found")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: ./main_0.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    check_user_id(employee_id)
