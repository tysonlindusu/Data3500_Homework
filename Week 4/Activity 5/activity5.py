"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""
#access the data
file = open('./AAPL.txt')
#convert it to an array
lines = file.readlines()
#initialize an array to hold our float values
price_float = []
#type cast the values to floats
for line in lines:
    price_float.append(float(line))
#initialize a value to hold our aggregate total of all prices
total_price = 0
#loop through our float values to add them to total_price
for i in price_float:
    total_price += i
#divide the total price by the number of items in the array to get the average
average_price = total_price / len(price_float)
#do the same thing for a five day total
five_day_total = 0
#add the values
for i in range(1,6):
    five_day_total += price_float[i]
#divide by 5 days
five_day_average = five_day_total / 5
#print the values
print(average_price)
print(five_day_average)