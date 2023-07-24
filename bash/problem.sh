#!/bin/bash

# Find employees in a specific department.
# Run by supplying a department.
# Ex. -> ./find_employees.sh Finance

# Check if the correct number of arguments (department name) is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <department>"
  exit 1
fi

# Get the department name from the command-line argument
department="$1"

grep "$department" employees.txt | awk -F ',' '{print $1}'
