"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
#import library
import random
#initialize array
number_list = []
#loop to assign random integers
for i in range(1,11):
    number_list.append(random.randint(1, 50))
#print
print(number_list)