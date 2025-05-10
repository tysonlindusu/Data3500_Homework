"""
1. Find all the prime numbers within a given range using a for loop

2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
"""

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num < 2:
        continue

    prime = True
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)