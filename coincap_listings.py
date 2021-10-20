import json
import requests

api_key = [
    "95551983-47f7-46d6-b224-63f7fddb43e8"
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
