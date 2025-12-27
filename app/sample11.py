def convert_dollars_to_rupees(dollars, rate=82.0):
    """
    Convert an amount in US dollars to Indian rupees.

    Args:
        dollars (float): Amount in USD.
        rate (float): Conversion rate (1 USD = rate INR). Default is 82.0.

    Returns:
        float: Equivalent amount in INR.
    """
    try:
        amount = float(dollars)
    except (TypeError, ValueError):
        raise ValueError("`dollars` must be a number")
    return amount * float(rate)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert US Dollars to Indian Rupees")
    parser.add_argument("dollars", nargs="?", type=float,
                        help="Amount in USD to convert (if not provided, you'll be prompted)")
    parser.add_argument("--rate", type=float, default=82.0,
                        help="Conversion rate: 1 USD = X INR (default: 82.0)")
    args = parser.parse_args()

    if args.dollars is None:
        try:
            raw = input("Enter amount in USD: ")
            usd = float(raw)
        except Exception:
            print("Invalid input. Please enter a numeric value for dollars.")
            raise SystemExit(1)
    else:
        usd = args.dollars

    inr = convert_dollars_to_rupees(usd, args.rate)
    print(f"{usd:.2f} USD = {inr:.2f} INR (rate: {args.rate})")