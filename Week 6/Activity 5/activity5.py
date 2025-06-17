"""
Programming Activity 5

Write a program, which loads a json file "person.json" into a Python 
dictionary. Change the contents of person["age"] by adding 1. Save the 
updated dictionary to person.json, and verify the contents of person.json 
have been updated.
- load person.json in to a Python dictionary using the json.load() function
- update the value of person["age"], increase by 1
- save the Python dictionary to person.json
- open person.json and verify the "age" value has increased by 1
"""

import json
import os

# Step 1: Get the full path to the JSON file in the current folder
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "person-1-1.json")

# Step 2: Load the JSON file into a Python dictionary
with open(file_path, "r") as file:
    person = json.load(file)

# Step 3: Increase the age by 1
person["age"] += 1

# Step 4: Save the updated dictionary back to the file
with open(file_path, "w") as file:
    json.dump(person, file, indent=4)

# Step 5: Open the file again to verify the age has been updated
with open(file_path, "r") as file:
    updated_person = json.load(file)
    print(f"Updated age: {updated_person['age']}")
