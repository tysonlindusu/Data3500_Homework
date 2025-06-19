"""
Each project must meet the following 6 project requirements:

Obtaining data from a web JSON API (40 points)
Storing the data in CSV files on your VS Code server and have the stored in GitHub (40 points)
The ability to add new data to your dataset.  Meaning, tomorrow you can run your program again, and it will go get the latest data, and run your analysis again. (40 points)
Perform analysis on the data. (30 points)
Store your results in a results.json file on your VS Code server and have the stored in GitHub (40 points)
Turn in a 2 - 4 minute video explaining and running your code - show your data updating (not overwriting) and how the results are shown (10 points)
  (Your program must also use good programming style and comments)
"""

#Final Project
# This project analyzes 6 cryptocurrencies using two trading strategies:
#Simple Moving Average
#Mean Reversion Strategy

#It fetches data from CoinGecko API, stores it in CSV files, runs analysis, and saves results to results.json
# Since we already developed strategies for mean reversion and simpel moving average, we can use these functions and their outputs for our cryptocurrency project strategy
# Some of the code previously written for HW4 and HW5 will be reused here.

import time
import requests
import json
import csv
import os
from datetime import datetime, timedelta
import statistics
from typing import Dict, List, Tuple

cryptocurrencies = [
    'bitcoin',
    'ethereum',
    'litecoin',
    'ripple',
    'binancecoin',
    'cardano'
]
#I chose coingecko because it was the first API that came up
#this has a rate limit of 5 - 15 calls per minute so I've slowed down the calls with time.sleep(5) but even then it will get rate limited if you run it
#multiple times too quickly. that will result in hitting the exception block and the api will respond with 'too many requests'
base_url = "https://api.coingecko.com/api/v3"
#define this folder's path
current_directory = os.path.dirname(os.path.abspath(__file__)) if __file__ else os.getcwd()

def fetch_data(crypto_name: str, days: int = 30) -> List[dict]:
    #fetch our crypto data
    url = f"{base_url}/coins/{crypto_name}/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily'
    }
    #usually a good idea to try/except async processes like fetching data across the internet
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()

        processed_data = []
        prices = data['prices']
        market_caps = data['market_caps']
        volumes = data['total_volumes']

        for i in range(len(prices)):
            processed_data.append({
                'date': datetime.fromtimestamp(prices[i][0] / 1000).strftime('%Y-%m-%d'),
                'price': round(prices[i][1], 8),
                'market_cap': round(market_caps[i][1], 2),
                'volume': round(volumes[i][1], 2)
            })
        #print how much data we got
        print(f"Successfully fetched {len(processed_data)} days of data for {crypto_name}")
        #return our data so we can save it in a variable
        return processed_data
    except requests.exceptions.RequestException as e:
        #print what the error was that was got if data couldn't return -- most likely API fetch limit error
        print(f"Error fetchign data for {crypto_name}: {e}")
        return []

def save_to_csv(crypto_name: str, data: List[dict]) -> None:
    #save data to csv file or update existing data

    filename = os.path.join(current_directory, f"{crypto_name}_data.csv")
    existing_data = {}
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_data[row['date']] = row

    for entry in data:
        existing_data[entry['date']] = entry
    
    with open(filename, 'w', newline='') as file:
        if existing_data:
            fieldnames = ['date', 'price', 'market_cap', 'volume']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            #write the data
            writer.writerows(existing_data.values())
        #output where we saved the file and what crypto it was for
        print(f"Data saved for {crypto_name} to {filename}")

def load_csv_data(crypto_name: str) -> List[dict]:
    filename = os.path.join(current_directory, f"{crypto_name}_data.csv")
    data = []

    if os.path.exists(filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['price'] = float(row['price'])
                row['market_cap'] = float(row['market_cap'])
                row['volume'] = float(row['volume'])
                data.append(row)
    return data

def sma_strategy(data: List[dict]) -> dict:
    if len(data) < 5:
        return {
            'strategy': 'SMA',
            'profit': 0,
            'percent_return': 0,
            'num_trades': 0,
            'trades': [],
            'current_signal': 'HOLD'
        }

    prices = [entry['price'] for entry in data]
    holding = False
    buy_price = None
    profit = 0
    first_buy = None
    trades = []

    print("Simple Moving Average Strategy Output:")

    for i in range(5, len(prices)):
        avg = sum(prices[i - 5: i]) / 5
        price = prices[i]

        if not holding and price > avg:
            buy_price = price
            if first_buy is None:
                first_buy = buy_price
            print(f"buying at:       {buy_price:.2f}")
            holding = True
            trades.append({
                'date': data[i]['date'],
                'action': 'BUY',
                'price': buy_price
            })
        elif holding and price < avg:
            sell_price = price
            trade_profit = round(sell_price - buy_price, 2)
            print(f"selling at:      {sell_price:.2f}")
            print(f"trade profit:    {trade_profit:.2f}")
            profit += trade_profit
            holding = False
            trades.append({
                'date': data[i]['date'],
                'action': 'SELL',
                'price': sell_price,
                'profit': trade_profit
            })

    print("-----------------------")
    print(f"Total profit:    {profit:.2f}")
    if first_buy:
        percent_return = round((profit / first_buy) * 100, 2)
        print(f"First buy:       {first_buy:.2f}")
        print(f"Percent return:  {percent_return}%")
    else:
        percent_return = 0
        print("No trades made.")

    # Determine current signal
    latest_avg = sum(prices[-5:]) / 5
    latest_price = prices[-1]
    if not holding and latest_price > latest_avg:
        signal = 'BUY'
    elif holding and latest_price < latest_avg:
        signal = 'SELL'
    else:
        signal = 'HOLD'

    return {
        'strategy': 'SMA',
        'profit': round(profit, 2),
        'percent_return': percent_return,
        'num_trades': len(trades),
        'trades': trades,
        'current_signal': signal
    }


def mr_strategy(data: List[dict]) -> dict:
    # if we don't have enough data, return a default object
    if len(data) < 5:
        return {'total_return': 0, 'trades': [], 'current_signal': 'HOLD', 'profit': 0, 'percent_return': 0}
    
    prices = [entry['price'] for entry in data]
    holding = False
    buy_price = None
    profit = 0
    first_buy = None
    trades = []
    
    print("Mean Reversion Strategy Output:")
    
    # Loop over data starting from 5th item
    for i in range(5, len(prices)):
        avg = sum(prices[i - 5:i]) / 5  # 5-day moving average
        price = prices[i]
        
        # Buy or sell logic
        if not holding and price < avg * 0.98:  # Buy when price is 2% below average
            buy_price = price
            if first_buy is None:
                first_buy = buy_price
            print(f"buying at:       {buy_price:.2f}")
            holding = True
            trades.append({
                'date': data[i]['date'],
                'action': 'BUY',
                'price': buy_price
            })
            
        elif holding and price > avg * 1.02:  # Sell when price is 2% above average
            sell_price = price
            trade_profit = round(sell_price - buy_price, 2)
            print(f"selling at:      {sell_price:.2f}")
            print(f"trade profit:    {trade_profit:.2f}")
            profit += trade_profit
            holding = False
            trades.append({
                'date': data[i]['date'],
                'action': 'SELL',
                'price': sell_price,
                'profit': trade_profit
            })
    
    # Calculate profit and print it
    print("-----------------------")
    print(f"Total profit:    {profit:.2f}")
    
    if first_buy:
        percent_return = round((profit / first_buy) * 100, 2)
        print(f"First buy:       {first_buy:.2f}")
        print(f"Percent return:  {percent_return}%")
    else:
        percent_return = 0
        print("No trades made.")
    
    # Determine current signal
    if len(prices) >= 5:
        latest_avg = sum(prices[-5:]) / 5
        latest_price = prices[-1]
        
        if not holding and latest_price < latest_avg * 0.98:
            signal = 'BUY'
        elif holding and latest_price > latest_avg * 1.02:
            signal = 'SELL'
        else:
            signal = 'HOLD'
    else:
        signal = 'HOLD'
    
    return {
        'strategy': 'Mean Reversion',
        'profit': round(profit, 2),
        'percent_return': percent_return,
        'num_trades': len(trades),
        'trades': trades,
        'current_signal': signal
    }

def analyze_crypto(crypto_name: str) -> dict:

    data = load_csv_data(crypto_name)

    if not data:
        print(f"No data available for {crypto_name}")
        return {}
    #get the result of trading with sma vs mean reversion
    sma_results = sma_strategy(data)
    mr_results = mr_strategy(data)

    if sma_results['current_signal'] in ['BUY', 'SELL']:
        print(f"SMA Strategy: You should {sma_results['current_signal']} {crypto_name} today")
    
    if mr_results['current_signal'] in ['BUY', 'SELL']:
        print(f"Mean Reversion Strategy: You should {mr_results['current_signal']} {crypto_name} today")

    return {
        'cryptocurrency': crypto_name,
        'data_points': len(data),
        'latest_price':data[-1]['price'] if data else 0,
        'latest_date': data[-1]['date'] if data else '',
        'strategies': {
            'sma': sma_results,
            'mean_reversion': mr_results
        }
    }

def calculate_basic_stats(data: List[dict]) -> dict:
    if not data:
        return {}
    prices = [entry['price'] for entry in data]
    volumes = [entry['volume'] for entry in data]
    market_caps = [entry['market_cap'] for entry in data]

    return {
        'price_stats': {
            'mean': round(statistics.mean(prices), 4),
            'median': round(statistics.median(prices), 4),
            'std_dev': round(statistics.stdev(prices), 4) if len(prices) > 1 else 0,
            'min': round(min(prices), 4),
            'max': round(max(prices), 4)
        },
        'volume_stats': {
            'mean': round(statistics.mean(volumes), 2),
            'median': round(statistics.median(volumes), 2),
            'std_dev': round(statistics.stdev(volumes), 2) if len(volumes) > 1 else 0
        },
        'market_cap_stats': {
            'mean': round(statistics.median(market_caps), 2),
            'median': round(statistics.median(market_caps), 2),
            'std_dev': round(statistics.stdev(market_caps), 2) if len(market_caps) > 1 else 0
        }
    }

def find_best_performers(results: dict) -> dict:
    best_crypto = None
    best_strategy = None
    best_return = float('-inf')
    #iterates through our results and finds the ones with the best values
    for crypto_name, crypto_results in results.items():
        if 'strategies' in crypto_results:
            for strategy_name, strategy_data in crypto_results['strategies'].items():
                if strategy_data['percent_return'] > best_return:
                    best_return = strategy_data['percent_return']
                    best_crypto = crypto_name
                    best_strategy = strategy_name
    return {
        'best_cryptocurrency': best_crypto,
        'best_strategy': best_strategy,
        'best_return_percent': best_return
    }

def save_results(results: dict) -> None:
    best_performers = find_best_performers(results)
    #save the current time as analysis_date
    #save how many cryptos we looked at
    #save the best performers calculated from our best performers function
    #save the results
    results_data = {
        'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cryptocurrencies_analyzed': len(cryptocurrencies),
        'best_performers': best_performers,
        'detailed_results': results
    }

    results_file = os.path.join(current_directory, "results.json")

    with open(results_file, 'w') as file:
        json.dump(results_data, file, indent=2)

    print(f"\n Results saved to {results_file}")

    #Print a summary
    print(f"{'='*50}\n")
    print("ANALYSIS SUMMARY")
    print(f"{'='*50}")
    print(f"Best CryptoCurrency: {best_performers['best_cryptocurrency']}")
    print(f"Best Strategy: {best_performers['best_strategy']}")
    print(f"Best Return: {best_performers['best_return_percent']:.2f}%")
    print(f"{'-'*50}")

#main function that calls everything else
def compare_and_save_cryptos(cryptocurrencies: List = []):
    #provide an output and return if no currencies are provided
    if len(cryptocurrencies) == 0:
        print("No cryptocurrencies provided. Please provide some currencies and try again.")
        return
    print("Starting Crypto Analysis...")
    print(f"Pulling data for {len(cryptocurrencies)} cryptocurrencies...")
    print(f"Cryptos to analyze are: {','.join(cryptocurrencies)}")

    print(f"Saving files to: {current_directory}")
    #store all the results here until written
    all_results = {}
    #loop through cryptocurrencies provided
    for crypto in cryptocurrencies:
        print(f"\n{'-'*50}")

        #fetch data
        data = fetch_data(crypto)
        #slow down the requests to increase the chance they don't get rejected
        if data:
            #save the data if we got any, otherwise this prints an exception if API is down
            save_to_csv(crypto, data)
        #run analysis
        analysis_results = analyze_crypto(crypto)
        if analysis_results:
            #add stat analysis
            #load the data that was saved
            csv_data = load_csv_data(crypto)
            #pass it to the calculate basic stats function
            stats = calculate_basic_stats(csv_data)
            #save it into analysis results under the key statistics
            analysis_results['statistics'] = stats
            #add this to a key by the name of the cryptocurrency to the all_results object
            all_results[crypto] = analysis_results
    #save all our results
    save_results(all_results)

    print(f"Analysis complete -- check the current directory for all data and results.json")
    print(f" {len(cryptocurrencies)} csv files were created")
    print("Analysis complete. Please look at results.json to review results")

compare_and_save_cryptos(cryptocurrencies)