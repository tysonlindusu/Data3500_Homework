import os
import csv

# Get the absolute path so we don't have to worry about typos
current_dir = os.path.dirname(os.path.abspath(__file__))
#append that to the filename in our local folder
csv_path = os.path.join(current_dir, "TSLA.csv")

prices = []

with open(csv_path, 'r') as infile:
    reader = csv.DictReader(infile)
    # Handle potential hidden characters in header
    close_key = next((k for k in reader.fieldnames if "Close" in k), None)
    if not close_key:
        raise KeyError("Could not find a 'Close' column in the CSV headers.")
    #clean up the price to make sure there's no extra characters on it and convert it to float and append it to the prices list
    for row in reader:
        price_str = row[close_key].replace('$', '').strip()
        prices.append(round(float(price_str), 2))

# Reverse prices so oldest comes first so we can pretend we're starting trading as of 1 year ago
prices.reverse()

# mean reversion strategy, I think -- please let me know if I don't have the right idea about what this strategy is supposed to do
# my understanding is that we're supposed to look at the average price in a 5 day range and then buy if we're below it and sell if it goes
# above the 5 day average
holding = False
buy_price = None
first_buy_price = None
total_profit = 0

#pretty header
print("TSLA Mean Reversion Strategy Output: March 2024 - March 2025")
#get our 5 day moving average and current price
for i in range(5, len(prices)):
    current_price = prices[i]
    avg_price = sum(prices[i - 5:i]) / 5
#determine if it's a buy
    if not holding and current_price < avg_price * 0.98:
        buy_price = current_price
        holding = True
        #handle if it's the first time we're buying
        if first_buy_price is None:
            first_buy_price = buy_price
        print(f"buying at:       {buy_price:.2f}")
#determine if it's a sell
    elif holding and current_price > avg_price * 1.02:
        sell_price = current_price
        trade_profit = round(sell_price - buy_price, 2)
        #calculate our trade profit after a sell
        total_profit += trade_profit
        holding = False
        print(f"selling at:      {sell_price:.2f}")
        print(f"trade profit:    {trade_profit:.2f}")

#Final summary
print("-----------------------")
print(f"Total profit:    {total_profit:.2f}")
if first_buy_price:
    final_return = (total_profit / first_buy_price) * 100
    print(f"First buy:       {first_buy_price:.2f}")
    print(f"% return:        {final_return:.2f}%")
else:
    #handle if somehow the price never dips above or below the average so we don't have exceptions
    print("No trades executed.")
