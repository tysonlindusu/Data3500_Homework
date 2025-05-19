"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homework.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""

#access the data -- I'm trying a different method than last time to immediately read it into a variable
with open('./AAPL.txt', 'r') as file:
    price_strings = file.readlines()
#convert it to an float, put it in an array and loop through each value as they're added to the array(list)
prices = [float(price.strip()) for price in price_strings]
#slice the array and sum it then divide it by the number of prices in the array(list)
first_four_avg = sum(prices[:4]) / 4
#slice the array and sum it then divide it by the number of prices in the array(list)
#in this case, we start from the back and tell it to grab the last four indices starting from the end of the array
last_four_avg = sum(prices[-4:]) / 4
print(f'First four day average {first_four_avg:.2f}')
print(f'Last four day average {last_four_avg:.2f}')
#initialize a profit variable
profit = 0
#initialize a list to hold our moving average
moving_average = []
#initialize a price where we buy
bought_at = 0
#are we currently holding stock?
hold = False

#start our loop on day 4 so we have enough days to get a four day average
for i in range(3, len(prices)):
    avg = sum(prices[i - 3:i + 1]) / 4
    moving_average.append(avg)
    price = prices[i]
    # SMA strategy
    if not hold and price > avg:
        # buy under these conditions, if I'm understanding how SMA works correctly
        buy_price = price
        hold = True
    elif hold and price < avg:
        # sell under these conditions, I believe
        profit += price - buy_price
        hold = False

# Step 7: Final profit
print(f"\nTotal profit from strategy: ${profit:.2f}")
