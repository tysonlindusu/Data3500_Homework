"""
Programming Activity 6

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""

#use for loop's internal variable to loop through

for i in range(5, 95):
    if i % 5 == 0:
        print(i)


# give the while loop an instantiated variable to loop over

i = 5

while i <= 95:
    if i % 5 == 0:
        print(i)
    i += 1