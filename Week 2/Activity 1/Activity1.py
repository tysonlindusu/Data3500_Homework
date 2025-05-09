apple_price = 0.75
number_purchased = 8
tax = 1.07
total_bill = apple_price * number_purchased * tax
if total_bill == 0:
    print("please check your inputs, your total_bill is equal to 0")
else:
    print("We purchased ", number_purchased, " apples for a total price of: ", total_bill)