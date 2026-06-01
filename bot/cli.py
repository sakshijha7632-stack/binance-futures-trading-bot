import argparse

from colorama import init, Fore

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

init()


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET, LIMIT or STOP_LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        required=False,
        help="Required for LIMIT and STOP_LIMIT orders"
    )

    parser.add_argument(
        "--stop-price",
        required=False,
        help="Required for STOP_LIMIT orders"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(
            args.side
        )

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        client = BinanceClient().client

        manager = OrderManager(client)

        if order_type == "MARKET":

            result = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        elif order_type == "LIMIT":

            if args.price is None:
                raise ValueError(
                    "LIMIT orders require --price"
                )

            result = manager.place_limit_order(
                symbol,
                side,
                quantity,
                args.price
            )

        elif order_type == "STOP_LIMIT":

            if args.price is None:
                raise ValueError(
                    "STOP_LIMIT orders require --price"
                )

            if args.stop_price is None:
                raise ValueError(
                    "STOP_LIMIT orders require --stop-price"
                )

            result = manager.place_stop_limit_order(
                symbol,
                side,
                quantity,
                args.price,
                args.stop_price
            )

        print("\n" + "=" * 40)
        print(Fore.GREEN + "ORDER PLACED SUCCESSFULLY")
        print(Fore.RESET + "=" * 40)

        print(f"Order ID     : {result.get('orderId')}")
        print(f"Symbol       : {result.get('symbol')}")
        print(f"Side         : {result.get('side')}")
        print(f"Status       : {result.get('status')}")
        print(f"Order Type   : {order_type}")
        print(f"Quantity     : {quantity}")

        avg_price = result.get("avgPrice")

        if avg_price and float(avg_price) > 0:
            print(f"Average Price: {avg_price}")

        print("=" * 40)

    except Exception as e:

        print("\n" + "=" * 40)
        print(Fore.RED + "ORDER FAILED")
        print(Fore.RESET + "=" * 40)
        print(Fore.RED + str(e))
        print(Fore.RESET + "=" * 40)


if __name__ == "__main__":
    main()