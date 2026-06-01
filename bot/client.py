from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
if not API_KEY or not SECRET_KEY:
    raise ValueError(
        "API credentials missing"
    )


class BinanceClient:

    def __init__(self):
        self.client = Client(
            API_KEY,
            SECRET_KEY,
            testnet=True
        )