import os
import csv
import sys
import json
import time
import requests
from datetime import datetime

local_currency = "USD"
local_symbol = "$"

api_key = '95551983-47f7-46d6-b224-63f7fddb43e8'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("ALERTS TRACKING...")
print()

already_hit_symbols = []

while True:
    with open("my_alerts.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[1] == "":
                continue
            if '\uffef' in line[0]:
                line[0] = line[0][1:].upper()
            else:
                line[0] = line[0].upper()
            symbol = line[0]
            amount = line[1]

            # print("SYMBOL: " + symbol)
            quote_url = base_url + "/v1/cryptocurrency/quotes/latest?convert=" + local_currency + "&symbol=" + symbol

            request = requests.get(quote_url, headers = headers)
            results = request.json()
            # print(json.dumps(results, sort_keys = True, indent = 4))

            currency = results["data"][symbol]
            # print(json.dumps(currency, sort_keys = True, indent = 4))
            name = currency["name"]
            price = currency["quote"][local_currency]["price"]

            if float(price) >- float(amount) and symbol not in already_hit_symbols:
                os.system("say ALERT ALERT ALERT")
                os.system("say " + name + " hit " + amount)
                sys.stdout.flush()

                now = datetime.now()
                current_time = now.strftime("%H:%M%p")
                print(name + " hit " + amount + " at " + current_time + "!")
                already_hit_symbols.append(symbol)
    print("...")
    time.sleep(10)
