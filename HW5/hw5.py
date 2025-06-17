#Homework 5
#You have to run the code by using "python3 hw5.py" from this folder, otherwise it doesn't seem to know that the pandas library is installed

import json
import os
import pandas as pd

#borrowed most of this logic from homework 4 since we're re-using mean reversion strategy, but implemented it into functions
def meanReversionStrategy(prices):
    holding = False
    buy_price = None
    profit = 0
    first_buy = None
    #loop over data
    print("Mean Reversion Strategy Output:")
    for i in range(5, len(prices)):
        avg = sum(prices[i - 5:i]) / 5
        price = prices[i]
    #buy or sell
        if not holding and price < avg * 0.98:
            buy_price = price
            if first_buy is None:
                first_buy = buy_price
            print(f"buying at:       {buy_price:.2f}")
            holding = True
        elif holding and price > avg * 1.02:
            sell_price = price
            trade_profit = round(sell_price - buy_price, 2)
            print(f"selling at:      {sell_price:.2f}")
            print(f"trade profit:    {trade_profit:.2f}")
            profit += trade_profit
            holding = False
    #calculate profit and print it, handle the first time we buy
    print("-----------------------")
    print(f"Total profit:    {profit:.2f}")
    if first_buy:
        percent_return = round((profit / first_buy) * 100, 2)
        print(f"First buy:       {first_buy:.2f}")
        print(f"Percent return:  {percent_return}%")
    else:
        percent_return = 0
        print("No trades made.")
    return round(profit, 2), percent_return
#we already wrote this more or less, so I've reused some of the same ideas
def simpleMovingAverageStrategy(prices):
    holding = False
    buy_price = None
    profit = 0
    first_buy = None
    #output our decision logic
    print("Simple Moving Average Strategy Output:")
    #start at 5th item in array and do a backwards window to check our moving prices
    for i in range(5, len(prices)):
        avg = sum(prices[i - 5:i]) / 5
        price = prices[i]
    #do we buy or sell or hold
        if not holding and price > avg:
            buy_price = price
            if first_buy is None:
                first_buy = buy_price
            print(f"buying at:       {buy_price:.2f}")
            holding = True
        elif holding and price < avg:
            sell_price = price
            trade_profit = round(sell_price - buy_price, 2)
            print(f"selling at:      {sell_price:.2f}")
            print(f"trade profit:    {trade_profit:.2f}")
            profit += trade_profit
            holding = False

    print("-----------------------")
    print(f"Total profit:    {profit:.2f}")
    if first_buy:
        percent_return = round((profit / first_buy) * 100, 2)
        print(f"First buy:       {first_buy:.2f}")
        print(f"Percent return:  {percent_return}%")
    else:
        percent_return = 0
        print("No trades made.")
    return round(profit, 2), percent_return
#save to a json file
def saveResults(results):
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)
#load our prices in from our json file after reversing the data so that we're looking at 1 year ago first, going up until today
def load_prices_from_csv(ticker):
    filename = f"{ticker}.csv"
    dfile = pd.read_csv(filename)
    dfile = dfile[::-1]  # reverse
    # strip "$" and convert to float
    dfile["Close/Last"] = dfile["Close/Last"].str.replace('$', '').astype(float)
    prices = dfile["Close/Last"].round(2).tolist()
    return prices

# Update with your 10 tickers
tickers = ["AAPL", "GOOG", "ADBE", "TSLA", "AMZN", "MSFT", "META", "CSCO", "BA", "JPM"]

results = {}

#generate our outputs by calling our functions
for ticker in tickers:
    print(f"\nloading and calculating {ticker}...\n")
    prices = load_prices_from_csv(ticker)
    results[f"{ticker}_prices"] = prices

    mr_profit, mr_returns = meanReversionStrategy(prices)
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = f"{mr_returns}%"

    sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = f"{sma_returns}%"

# save the full dictionary of results in a json file
saveResults(results)
