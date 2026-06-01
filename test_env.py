from dotenv import load_dotenv
import os

print("Current directory:", os.getcwd())
print("Env file exists:", os.path.exists(".env"))

load_dotenv(".env")

print("API KEY =", os.getenv("BINANCE_API_KEY"))
print("SECRET =", os.getenv("BINANCE_SECRET_KEY"))