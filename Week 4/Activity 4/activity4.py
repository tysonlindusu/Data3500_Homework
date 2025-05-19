"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""

#import our library
import random
#initialize our variables
number_list = []
last_was_even = False
#loop through and append our random numbers
for i in range(1,11):
    number_list.append(random.randint(1, 50))
#use our variable to store whether the last number was even and then check on the next loop if the current one was even
# if both were even, print it out, if not, then set the value of last_was_even back to false if you're looping over an odd number
for i in number_list:
    print(f'checking number {i}')
    if(i % 2 == 0 and last_was_even == True):
        print('Found two even numbers in a row')
        break
    elif(i % 2 == 0):
        last_was_even = True
    else:
        last_was_even = False