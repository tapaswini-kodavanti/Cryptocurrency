import json
import requests

api_key = [
    '95551983-47f7-46d6-b224-63f7fddb43e8'
]

while(True):
    # Same as listings_url
    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='+api_key[0]

    limit = 5000
    start = 1
    sort = 'market_cap'
    convert = 'USD'

    choice = input("Do you want to enter any custom parameter? (y/n): ")
    if choice == "y":
        limit = input("Limit is currently " + str(limit) + ". What is the custom limit?: ")
        start = input("Start is currently " + str(start) + ". What is the custom start number?: ")
        sort = input("Sorting is by " + sort + ". What do you want to sort by?: ")
        convert = input("Currency is set to " + convert + ". What is your local currency?: ")


    ticker_url += '&limit=' + str(limit) + '&start=' + str(start) + '&sort=' + sort + '&convert=' + convert
    request = requests.get(ticker_url)
    results = request.json()


    data = results['data']

    print()
    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']

        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])
        try:
            percent_coins_in_circulation = int(circulating_supply/total_supply)
        except ZeroDivisionError:
            percent_coins_in_circulation = "Unknown"

        quotes = currency['quote'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        volume_string = '{:,}'.format(volume)
        market_cap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(total_supply)

        print(str(rank) + ": " + name + "(" + symbol + ")")
        print("Market cap: \t\t$" + market_cap_string)
        print("Price: \t\t\t$" + str(price))
        print("24h Volume: \t\t" + volume_string)
        print("Hour change: \t\t" + str(hour_change) + "%")
        print("Day change: \t\t" + str(day_change) + "%")
        print("Week change: \t\t" + str(week_change) + "%")
        print("Total supply: \t\t" + total_supply_string)
        print("Circulating supply: \t" + circulating_supply_string)
        print("Percentage of coins in circulation: " + str(int(circulating_supply / total_supply * 100)))
        print()

    choice = input("Again? (y/n): ")

    if choice == "n":
        break
