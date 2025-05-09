# WHAT DOES THIS CODE DO? Create the variables x = 2 and y = 3, then determine what each of the following statements displays:
# define the variable x and set its value to 2 which will be stored as an integer I would guess
x = 2
# yep, it's an integer
print(type(x))
# define y as an integer
y = 3
# prints the string x = followed by the value of the variable x
print('x =', x)
# prints Value of followed by the variable x's value followed by the string + following by the variable x's value followed by the string is followed by the variable x's value
# added to itself (multiplied by 2)
print('Value of', x, '+', x, 'is', (x + x))
# just prints the string x =
print('x =')
# prints the sum of the values associated with variables x and y, followed by the string x = followed by the sum of the values associated with variables y + x
print((x + y), 'x =', (y + x))