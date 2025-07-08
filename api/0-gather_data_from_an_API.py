#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
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

        # Filter completed tasks
        completed_tasks = [task for task in todos if task.get('completed')]

        # Output
        total_tasks = len(todos)
        done_tasks = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException as e:
        print("Error while connecting to the API:", e)
    except ValueError:
        print("Invalid response format.")
    except IndexError:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
