import math
import json
import locale
import requests
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

local_currency = "USD"
local_symbol = "$"

api_key = 'Your API Key Here'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(global_url, headers = headers)
results = request.json()

data = results["data"]

# Finding data in jSON tree
total_market_cap = data["quote"][local_currency]["total_market_cap"]
total_market_cap_string = "{:,}".format(total_market_cap)

# (Last 3 Columns)
# Display the value of that cryptocurrency if the global market cap reaches the level designated to that columns
# For example, what would the price of Bitcoin be if the global market cap was $10.9 trillion, the gold price level?
table = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Price', '10.9T (Gold)', '35.2T (Narrow Money)', '89.5T (Stock Market)'])

listings_url = base_url + "/v1/cryptocurrency/listings/latest?convert=" + local_currency

request = requests.get(listings_url, headers=headers)
results = request.json()

data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']

    market_cap = currency['quote'][local_currency]['market_cap']

    percentage_of_global_cap = float(market_cap) / float(total_market_cap)

    price = currency['quote'][local_currency]['price']

    available_supply = currency['total_supply']

    # To determine the price of a cryptocurrency at a given commodity price level (for example, gold),
    # multiply the commodity price by the percent of the global market cap and divide by available supply
    # to find the price of one whole cryptocurrency

    gold_price = 10900000000000 * percentage_of_global_cap / available_supply
    narrow_money_price = 35000000000000 * percentage_of_global_cap / available_supply
    stock_market_price = 89500000000000 * percentage_of_global_cap / available_supply

    percentage_of_global_cap_string = str(round(percentage_of_global_cap *100, 2)) + "%"
    price_string = local_symbol + "{:,}".format(round(price, 2))
    gold_price_string = local_symbol + "{:,}".format(round(gold_price, 2))
    narrow_money_price_string = local_symbol + "{:,}".format(round(narrow_money_price, 2))
    stock_market_price_string = local_symbol + "{:,}".format(round(stock_market_price, 2))

    table.add_row([name, ticker, percentage_of_global_cap_string, price_string, gold_price_string, narrow_money_price_string, stock_market_price_string])


print()
print(table)
print()
