#!/usr/bin/python3

import json

# Sample data structure with all user IDs from 1 to 10
employees_tasks = {
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": False}
    ],
    "2": [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": True}
    ],
    "3": [
        {"username": "Samantha", "task": "Example task for Samantha", "completed": False}
    ],
    "4": [
        {"username": "Karianne", "task": "Example task for Karianne", "completed": True}
    ],
    "5": [
        {"username": "Kamren", "task": "Example task for Kamren", "completed": False}
    ],
    "6": [
        {"username": "Leopoldo_Corkery", "task": "Example task for Leopoldo_Corkery", "completed": False}
    ],
    "7": [
        {"username": "Elwyn.Skiles", "task": "Example task for Elwyn.Skiles", "completed": True}
    ],
    "8": [
        {"username": "Maxime_Nienow", "task": "Example task for Maxime_Nienow", "completed": False}
    ],
    "9": [
        {"username": "Delphine", "task": "Example task for Delphine", "completed": True}
    ],
    "10": [
        {"username": "Moriah.Stanton", "task": "Example task for Moriah.Stanton", "completed": False}
    ]
}

# Exporting data to JSON format
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(employees_tasks, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")
