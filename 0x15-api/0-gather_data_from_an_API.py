#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if "name" not in employee_data:
        print("Employee not found.")
        return

    employee_name = employee_data["name"]

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task["completed"]]
    number_of_completed_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks ({number_of_completed_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

employee_id = 1
get_employee_todo_progress(employee_id)
