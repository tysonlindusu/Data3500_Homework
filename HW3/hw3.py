"""
3.4 (Fill in the Missing Code) In the code below
for ***:
    for ***:
        print('@')
    print()
replace the *** so that when you execute the code, it displays two rows, each containing seven @ symbols, as in:

@@@@@@@
@@@@@@@
"""

#3.4
print('======================== 3.4 ========================')

#nested loop that prints @ 7 times and it does all of that twice
for i in range(2):
    for j in range(7):
        print('@', end='')
    print()


"""
3.9 (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated 
a five-digit integer into its individual digits and displayed them. Reimplement your script 
to use a loop that in each iteration “picks off” one digit (left to right) using the // and % 
operators, then displays that digit.
"""

#3.9
print('======================== 3.9 ========================')

print('Please enter a 5 digit number:')
number = int(input())
#make sure the number is valid, then yoink each digit and print it and then adjust the floor divisor so it will grab the next number on the following loop
if 10000 <= number <= 99999:
    floor_divisor = 10000

    while floor_divisor >= 1:
        digit = (number // floor_divisor) % 10
        print(digit, end='    ')
        floor_divisor = floor_divisor // 10
else:
    print('Please enter a valid fix-digit number')

"""
3.11 (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles. One driver 
has kept track of several tankfuls of gasoline by recording miles driven and gallons
used for each tankful. Develop a sentinel-controlled-repetition script that prompts
 the user to input the miles driven and gallons used for each tankful. The script should
  calculate and display the miles per gallon obtained for each tankful. After processing 
  all input information, the script should calculate and display the combined miles per gallon 
  obtained for all tankfuls (that is, total miles driven divided by total gallons used).

Enter the gallons used (-1 to end): 12.8

Enter the miles driven: 287

The miles/gallon for this tank was 22.421875

Enter the gallons used (-1 to end): 10.3

Enter the miles driven: 200

The miles/gallon for this tank was 19.417475

Enter the gallons used (-1 to end): 5

Enter the miles driven: 120

The miles/gallon for this tank was 24.000000

Enter the gallons used (-1 to end): -1

The overall average miles/gallon was 21.601423
"""

#3.11
print('======================== 3.11 ========================')

total_miles = 0
total_gallons = 0

#loop through each tank of gas the user inputs
while True:
    gallons = float(input("Enter the gallons used (-1 to end): "))
    if gallons == -1:
        break

    miles = float(input('Enter the miles driven: '))
    mpg = miles / gallons
    #tell the user how that tank of gas performed
    print(f"The miles/gallon for this tank was {mpg:.6f}")

    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    #tell the user how all tanks of gas averaged out
    print(f"\nThe overall miles/gallons was {overall_mpg:.6f}")
else:
    print('\nNo input')

"""
3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same backwards
 or forwards. For example, each of the following five-digit integers is a palindrome: 12321, 
 55555, 45554 and 11611. Write a script that reads in a five-digit integer and determines whether
  it’s a palindrome. [Hint: Use the // and % operators to separate the number into its digits.]
"""

#3.12
print('======================== 3.12 ========================')


number = int(input("Enter a five-digit number: "))
#make sure it's a valid number, then separate out each number, stored into its own variable
if 10000 <= number <= 99999:
    first = number // 10000
    second = (number // 1000) % 10
    fourth = (number // 10) % 10
    fifth = number % 10
# check the appropriate variables to see if it's a palindrome
    if first == fifth and second == fourth:
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
else:
    #if it wasn't valid input, let the user know
    print("Invalid input. Please enter a five-digit number.")


"""
3.14 (Challenge: Approximating the Mathematical Constant π) Write a script that computes
 the value of π from the following infinite series. Print a table that shows the value of
  π approximated by one term of this series, by two terms, by three terms, and so on. How 
  many terms of this series do you have to use before you first get 3.14? 3.141? 3.1415? 3.14159?

value of pi
"""

#3.14
print('======================== 3.14 ========================')

#define our variables that we'll need for the program, initializing each
numeric_pi = 0
target_pi = ""
denominator = 1
sign = 1
term = 0

two_decimals_twice = 0
times_seen_counter = 0

print("Term\t Approximation of pi")

#we keep looping through the pattern that was given until we reach 3.14159. In order to make it easier to truncate to the number of decimal
#places, I converted to a string so I could use python's floating point formatting syntax
while target_pi != "3.141":
    term += 1
    numeric_pi += sign * (4 / denominator)
    target_pi = f"{numeric_pi:.3f}"
    target_two_pi = f"{numeric_pi:.2f}"
    if target_two_pi == "3.14":
        times_seen_counter += 1
    if times_seen_counter == 2:
        two_decimals_twice = term
    print(f"{term}\t{numeric_pi:.10f}")
    denominator += 2
    sign *= -1
    
print(f"It took {term} terms to arrive at {target_pi}")
print(f"it took {two_decimals_twice} terms to hit 3.14 twice")