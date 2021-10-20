import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = "USD"

api_key = [
    "Insert your key"
]

listing_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY="+api_key[0] + "&convert=" + convert

request = requests.get(listings_url)
results = request.json()
data = results["data"]

# Creates Key-Data pairs for easy access when requesting with ticker symbol of cryptocurrency
ticker_url_pairs = {}

for currency in data:
    symbol = currency["symbol"]
    url = currency["id"]
    ticker_url_pairs[symbol] = url


print()
print("MY PORTFOLIO")
print()

portfolio_value = 0.00
last_updated = 0

table = PrettyTable(["Asset", "Amount Owned", convert + "Value", "Price", "1h", "24h", "7d"])

with open("portfolio.txt") as inp:
    for line in inp:
        ticker, amount = line.split()
        ticker = ticker.upper()

        ticker_url =
