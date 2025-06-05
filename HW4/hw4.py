import os
import csv

# Get the path so we don't have to worry about typos
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

    for row in reader:
        price_str = row[close_key].replace('$', '').strip()
        prices.append(round(float(price_str), 2))

# Step 2: Reverse prices so oldest comes first
prices.reverse()

# Step 3: Run mean reversion strategy
holding = False
buy_price = None
first_buy_price = None
total_profit = 0

print("TSLA Mean Reversion Strategy Output: March 2024 - March 2025")

for i in range(5, len(prices)):
    current_price = prices[i]
    avg_price = sum(prices[i - 5:i]) / 5

    if not holding and current_price < avg_price * 0.98:
        buy_price = current_price
        holding = True
        if first_buy_price is None:
            first_buy_price = buy_price
        print(f"buying at:       {buy_price:.2f}")

    elif holding and current_price > avg_price * 1.02:
        sell_price = current_price
        trade_profit = round(sell_price - buy_price, 2)
        total_profit += trade_profit
        holding = False
        print(f"selling at:      {sell_price:.2f}")
        print(f"trade profit:    {trade_profit:.2f}")

# Step 4: Final summary
print("-----------------------")
print(f"Total profit:    {total_profit:.2f}")
if first_buy_price:
    final_return = (total_profit / first_buy_price) * 100
    print(f"First buy:       {first_buy_price:.2f}")
    print(f"% return:        {final_return:.2f}%")
else:
    print("No trades executed.")
