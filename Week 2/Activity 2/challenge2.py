a = input("Enter a number")
b = input("Enter a second number")
c = input("Enter a third number")

a = int(a)
b = int(b)
c = int(c)

min_value = min(a,b,c)
max_value = max(a,b,c)
if max_value % 2 == 0:
    for i in range(min_value, max_value):
        print(i)
elif max_value % 2 != 0:
    if min_value >= 0 and min_value <= 10:
        print('min value is between 0 and 10')
    else:
        print('min value is not between 0 and 10')