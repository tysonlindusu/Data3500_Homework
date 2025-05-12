"""
1. Write a Python program that checks the strength of a user's password. Password strength is determined by the following rules:

The password must be at least 8 characters long.
The password must contain at least one uppercase letter.
The password must contain at least one lowercase letter.
The password must contain at least one digit.
The password may contain special characters (e.g., !, @, #, $, etc.), but it is not required.
Your program should prompt the user to enter a password, and then it should determine whether the password meets these criteria.

Example Input/Output:
# Input
password = "SecureP@ssw0rd"
# Output
Password is strong!

# Input
password = "weak"
# Output
Password is weak. It does not meet the criteria.


2. You are building a weather decision-making system for a camping trip. To decide whether to go camping, you need to consider the weather conditions and other factors. You will make the decision based on the following criteria:

The weather should be either clear or partly cloudy.
The temperature should be between 50°F (10°C) and 85°F (30°C).
It should not be raining or snowing.
It should not be too windy (wind speed less than 20 mph).
Your program should prompt the user to enter the current weather conditions, temperature, and wind speed, and then determine whether it's a good day to go camping.

Write a Python program for weather-based decision-making that takes weather conditions, temperature, and wind speed as input and checks if it's a good day for camping based on the criteria above. Display a message indicating whether it's a good day to go camping or not.
"""

# Secure password checker

import re

not_valid_password = True

while not_valid_password == True:
    print('Please enter a password: ')
    password = input()

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

    if re.match(pattern, password):
        print('Password is strong!')
        not_valid_password = False
    else:
        print('Password is weak. It does not meet the criteria.')

# Weather decision-making system
# I did not add input validation to this

def should_i_camp(temp,weather_conditions,windy):
    match weather_conditions:
        case "y":
            weather_conditions = True
        case "n":
            weather_conditions = False
    if 50 < temp < 85 and weather_conditions == False and windy < 20:
        return "It's a good day to camp."
    else:
        return "It's not a good day to camp."

print('Please enter the temperature in Fahrenheit: ')
temp = int(input())
print('Please indicate whether it is raining or snowing (y/n)')
weather_conditions = input()
print('Please input how fast the wind is blowing today')
windiness = int(input())

decision = should_i_camp(temp, weather_conditions,windiness)

print(decision)