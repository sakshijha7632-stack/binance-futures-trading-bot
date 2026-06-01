from bot.client import BinanceClient

client = BinanceClient().client

try:
    account_info = client.futures_account()

    print("Connected successfully!")
    print(account_info)

except Exception as e:
    print("Connection failed:")
    print(e)