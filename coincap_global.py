import json
import requests
from datetime import datetime

currency = "USD"

api_key = [
    "Insert your key"
]

global_url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?CMC_PRO_API_KEY="+api_key[0]+"&convert="+currency

request = requests.get(global_url)
results = request.json()


active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_market_pairs']
bitcoin_percentage = results['data']['btc_dominance']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quote'][currency]['total_market_cap'])
global_volume = int(results['data']['quote'][currency]['total_volume_24h'])

active_currencies_string = "{:,}".format(active_currencies)
active_markets_string = "{:,}".format(active_markets)
global_cap_string = "{:,}".format(global_cap)
global_volume_string = "{:,}".format(global_volume)

# last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print("There are currently " + active_currencies_string + " active cryptocurrencies and " + active_markets_string +  " active markets.")
print("The global cap of all cryptos is " + global_cap_string + " and the 24h global volume is " + global_volume_string + ".")
print("Bitcoin\'s total percentage of the global cap is " + str(bitcoin_percentage) + "%.")
print()
print("This information was last updated on " + last_updated + ".")
