#!/usr/bin/python3

import json

# Sample data structure with all user IDs from 1 to 10 and specific tasks
employees_tasks = {
    "1": [
        {"username": "Bret", "task": "Specific task for Bret 1", "completed": False},
        {"username": "Bret", "task": "Specific task for Bret 2", "completed": False}
    ],
    "2": [
        {"username": "Antonette", "task": "Specific task for Antonette 1", "completed": False},
        {"username": "Antonette", "task": "Specific task for Antonette 2", "completed": True}
    ],
    "3": [
        {"username": "Samantha", "task": "Specific task for Samantha", "completed": False}
    ],
    "4": [
        {"username": "Karianne", "task": "Specific task for Karianne", "completed": True}
    ],
    "5": [
        {"username": "Kamren", "task": "Specific task for Kamren", "completed": False}
    ],
    "6": [
        {"username": "Leopoldo_Corkery", "task": "Specific task for Leopoldo_Corkery", "completed": False}
    ],
    "7": [
        {"username": "Elwyn.Skiles", "task": "Specific task for Elwyn.Skiles", "completed": True}
    ],
    "8": [
        {"username": "Maxime_Nienow", "task": "Specific task for Maxime_Nienow", "completed": False}
    ],
    "9": [
        {"username": "Delphine", "task": "Specific task for Delphine", "completed": True}
    ],
    "10": [
        {"username": "Moriah.Stanton", "task": "Specific task for Moriah.Stanton", "completed": False}
    ]
}

# Exporting data to JSON format
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(employees_tasks, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")
