#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a given employee ID
using the JSONPlaceholder REST API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches the employee’s TODO list and displays progress.
    """
    try:
        # Fetch employee details
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch TODO tasks
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Count total and completed tasks
        total_tasks = len(todos)
        completed_tasks = [task for task in todos if task.get('completed')]
        done_tasks = len(completed_tasks)

        # Display progress
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException as e:
        print("Error while connecting to the API:", e)
    except ValueError:
        print("Invalid response format.")
    except KeyError:
        print("Unexpected data structure.")
    except Exception as e:
        print("Unexpected error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
