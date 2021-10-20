import json
import requests

api_key = [
    "Insert your key"
]

listing_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY="+api_key[0]

request = requests.get(listing_url)
results = request.json()

data = results['data']

for currency in data:
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ": " + name + "(" + symbol + ")")
