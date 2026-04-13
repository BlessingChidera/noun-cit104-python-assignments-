# ── Program 3: BMI calculator ────────────────────────────────────

# Ask for weight in kilograms
weight = float(input("Enter your weight (in kg): "))

# Ask for height in metres
height = float(input("Enter your height (in metres, e.g. 1.75): "))

# The BMI formula: weight divided by (height × height)
bmi = weight / (height ** 2)

# Now check which category the BMI falls into
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25.0:
    category = "Normal weight"
elif bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"

# Show the BMI value and the category
print(f"Your BMI is {bmi:.2f} — {category}")