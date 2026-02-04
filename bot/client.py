import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)

        # IMPORTANT: Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logger.info("Initialized Binance Futures Testnet client")

    def place_order(self, **order_params):
        """
        Places an order on Binance Futures Testnet
        """
        try:
            logger.info(f"Placing order with params: {order_params}")

            response = self.client.futures_create_order(**order_params)

            logger.info(f"Order placed successfully: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(
                f"Binance API Error | Status: {e.status_code} | Message: {e.message}"
            )
            raise

        except Exception as e:
            logger.exception("Unexpected error while placing order")
            raise
