def build_order_payload(args):
    payload = {
        "symbol": args.symbol.upper(),
        "side": args.side,
        "quantity": args.quantity,
    }

    if args.order_type == "MARKET":
        payload["type"] = "MARKET"

    elif args.order_type == "LIMIT":
        payload["type"] = "LIMIT"
        payload["price"] = args.price
        payload["timeInForce"] = "GTC"

    elif args.order_type == "STOP_LIMIT":
        payload["type"] = "STOP"
        payload["price"] = args.price
        payload["stopPrice"] = args.stop_price
        payload["timeInForce"] = "GTC"

    return payload
