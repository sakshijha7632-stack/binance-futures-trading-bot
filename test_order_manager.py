from bot.client import BinanceClient
from bot.orders import OrderManager

client = BinanceClient().client

manager = OrderManager(client)

print("OrderManager loaded successfully!")