# ── Program 4: Rectangle area and perimeter ──────────────────────

# Ask for the length
length = float(input("Enter the length of the rectangle: "))

# Ask for the breadth
breadth = float(input("Enter the breadth of the rectangle: "))

# Area = length times breadth
area = length * breadth

# Perimeter = 2 times (length + breadth)
perimeter = 2 * (length + breadth)

# Show both results
print(f"Area      = {area}")
print(f"Perimeter = {perimeter}")