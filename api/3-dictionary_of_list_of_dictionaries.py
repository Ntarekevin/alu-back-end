#!/usr/bin/python3

import json

# Sample data structure
employees_tasks = {
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui",
         "completed": False},
        # Add more tasks for user with ID 1 here
    ],
    "2": [
        {"username": "Antonette",
         "task": "suscipit repellat esse quibusdam voluptatem incidunt",
         "completed": False},
        {"username": "Antonette",
         "task": "distinctio vitae autem nihil ut molestias quo",
         "completed": True},
        # Add more tasks for user with ID 2 here
    ],
    # Add more users and their tasks here
}

# Exporting data to JSON format
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(employees_tasks, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")
