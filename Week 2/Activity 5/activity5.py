"""
Programming Activity 5:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""

#lets start with a function again
def decrease_and_print_age():
    user_age = int(input("How old are you?"))
    current_year = 2025

    while user_age > 0:
        print(f'you were alive in {current_year}')
        user_age -= 1
        current_year -= 1
    print(f"you were born in {current_year} or {current_year - 1} (depending on whether you've had your birthday yet this year)")

decrease_and_print_age()