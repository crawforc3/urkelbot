import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=10"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

for coin in crypto_list:
    if coin["symbol"] == "BTC":
        btc_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "ETH":
        eth_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "BCH":
        bch_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "BTG":
        btg_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "LTC":
        ltc_price = round(float(coin["price_usd"]), 2)

crypto_output = "<b>BTC</b>: ${}\n<b>BCH</b>: ${}\n<b>ETH</b>: ${}\n<b>BCG</b>: ${}\n<b>LTC</b>: ${}".format(btc_price, bch_price, eth_price, btg_price, ltc_price)

print(crypto_output)