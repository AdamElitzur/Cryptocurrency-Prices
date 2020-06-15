import requests

crypto = input("What Cryptocurrency Ticker would you like to know the price of? ").upper()
url = 'https://api.binance.com/api/v1/ticker/price?symbol=' + crypto + "USDT"
response = requests.get(
    url,
    headers = {"Accept": "application/json"}
).json()

price = response["price"]
print(price)
