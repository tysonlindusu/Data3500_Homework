"""
Programming Activity 2

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""

total = 0.0

denominator = 2.0

for i in range(1,1001):
    total += (1 / denominator)
    denominator *= 2

print('The total is: ', total)