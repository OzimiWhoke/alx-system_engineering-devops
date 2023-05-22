#!/usr/bin/python3
"""extend the Python script to export data in the CSV format"""

import csv
import requests

def export_employee_todo_to_csv(employee_id):
    # Base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetching employee information
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if "name" not in employee_data:
        print("Employee not found.")
        return

    employee_name = employee_data["name"]
    user_id = employee_data["id"]

    # Fetching employee's TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data for CSV export
    csv_data = []
    for task in todos_data:
        task_id = task["id"]
        task_title = task["title"]
        task_completed = task["completed"]
        csv_data.append([user_id, employee_name, task_completed, task_title])

    # Export data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)

    print(f"Data exported to {filename} successfully.")

# Test with employee ID 1
employee_id = 1
export_employee_todo_to_csv(employee_id)


