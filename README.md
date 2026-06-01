# Binance Futures Trading Bot

A Python CLI trading bot for Binance Futures Testnet.

## Features

- Market Orders
- Limit Orders
- Input Validation
- Logging
- Environment Variable Support
- Binance Futures API Integration

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

## Usage

### Market Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

### Limit Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type LIMIT \
--quantity 0.001 \
--price 50000
```
## Supported Order Types

- MARKET
- LIMIT
- STOP_LIMIT (Bonus Feature)

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── cli.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── 
│
├── requirements.txt
├── README.md
├── .gitignore
