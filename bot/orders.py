import logging


class OrderManager:

    def __init__(self, client):
        self.client = client


    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logging.info(
                f"Market Order: {response}"
            )

            return response

        except Exception as e:

            logging.error(str(e))
            raise


    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logging.info(
                f"Limit Order: {response}"
            )

            return response

        except Exception as e:

            logging.error(str(e))
            raise


    def place_stop_limit_order(
        self,
        symbol,
        side,
        quantity,
        price,
        stop_price
    ):

        try:

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

            logging.info(
                f"Stop Limit Order: {response}"
            )

            return response

        except Exception as e:

            logging.error(str(e))
            raise