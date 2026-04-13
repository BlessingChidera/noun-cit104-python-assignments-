# ── Program 1: USD to NGN converter ──────────────────────────────

# Ask the user to type in a dollar amount
usd_amount = float(input("Enter the amount in USD: "))

# Ask the user to type in today's exchange rate
exchange_rate = float(input("Enter the current exchange rate (1 USD = ? NGN): "))

# Multiply the two numbers to get the Naira amount
ngn_amount = usd_amount * exchange_rate

# Show the result to the user
print(f"{usd_amount} USD = {ngn_amount:,.2f} NGN")