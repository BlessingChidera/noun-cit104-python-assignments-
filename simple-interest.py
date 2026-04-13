# ── Program 2: Simple interest calculator ────────────────────────

# Ask the user to enter the loan amount (principal)
principal = float(input("Enter the principal (loan amount): "))

# Ask for the interest rate (as a percentage, e.g. 5 for 5%)
rate = float(input("Enter the rate (in %): "))

# Ask for how many years
time = float(input("Enter the time (in years): "))

# Apply the formula from your lecturer: SI = (P × R × T) / 100
simple_interest = (principal * rate * time) / 100

# Show the result
print(f"Simple Interest = {simple_interest:,.2f}")