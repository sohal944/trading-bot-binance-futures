import argparse
import os
import sys
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.validators import validate_order_args
from bot.orders import build_order_payload
from bot.logging_config import setup_logging


def main():
    # Setup logging first
    setup_logging()

    # Load environment variables
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument(
    "--order-type",
    required=True,
    choices=["MARKET", "LIMIT", "STOP_LIMIT"]
)

    parser.add_argument("--stop-price", type=float, help="Required for STOP_LIMIT orders")

    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # Validate input
        validate_order_args(args)

        # Initialize client
        client = BinanceFuturesClient(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
        )

        # Build order
        order_payload = build_order_payload(args)

        print("\n📤 Order Request Summary")
        for k, v in order_payload.items():
            print(f"{k}: {v}")

        # Place order
        response = client.place_order(**order_payload)

        print("\n✅ Order Placed Successfully")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Average Price : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
