import requests
from bs4 import BeautifulSoup

crypto = input("What cryptocurrency would you like to know the price of? ")
def cost(ticker):
    """Finds the price of the ticker"""
    url = 'https://api.binance.com/api/v1/ticker/price?symbol=' + ticker.upper() + "USDT"
    response = requests.get(
        url,
        headers = {"Accept": "application/json"}
        ).json()
    price = response["price"]
    return f"The price of {ticker} is ${price}"

def convert(name):
    """If the user input isn't a crypto's ticker, but its name, like Bitcoin instead of BTC, this function will convert it"""
    tickers = requests.get('https://coinmarketcap.com/currencies/' + name.lower())
    soup = BeautifulSoup(tickers.text, "html.parser")
    el = soup.find(class_ = 'cmc-details-panel-header sc-1extin6-0 gMbCkP')
    y = el.find_all('span')[1]
    text = y.get_text()
    ticker = text[1:-1]
    return cost(ticker)

try:
    try:
        print(cost(crypto))
    except:
        print(convert(crypto))
except:
    raise ValueError("That cryptocurrency is not supported on Binance")
