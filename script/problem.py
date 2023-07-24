#!/usr/bin/env python3

import sys

# Check if the correct number of arguments (department name) is provided
if len(sys.argv) != 2:
    print("Usage: {} <department>".format(sys.argv[0]))
    sys.exit(1)

# Get the department name from the command-line argument
department = sys.argv[1]

# Open the "employees.txt" file and read its content
with open("employees.txt", "r") as file:
    # Iterate through each line and check if the department name is present
    for line in file:
        # Split the line by commas to get individual fields
        name, age, gender, dept = line.strip().split(',')
        # If the department matches the input, print the employee name
        if dept == department:
            print(name)