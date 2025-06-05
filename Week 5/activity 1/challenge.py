"""
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

# Load the list of people from JSON
with open("person-1.json", "r") as file:
    people = json.load(file)
    for person in people:
        person["age"] += 1  # Increment each person's age

# Save the updated list back to the file
with open("person-1.json", "w") as file:
    json.dump(people, file, indent=4)  # <-- use 'people' not 'person'

# Reload and verify
with open("person-1.json", "r") as file:
    updated_people = json.load(file)
    for person in updated_people:
        print(f"updated age for: {person["name"]}, {person["age"]}")

