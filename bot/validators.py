def validate_order_args(args):
    """
    Validates CLI arguments before placing an order
    """

    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if args.side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")

    if args.order_type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

    if args.order_type == "MARKET" and args.price is not None:
        raise ValueError("Price should not be provided for MARKET orders")
    

    if args.order_type == "STOP_LIMIT":
     if args.price is None or args.stop_price is None:
        raise ValueError("STOP_LIMIT orders require both price and stop_price")

