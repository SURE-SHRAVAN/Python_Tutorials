num_fractions = int(input("Enter number of fractions: "))

fractions = []

# Loop to get each fraction
for i in range(num_fractions):
    num = int(input(f"Enter the numerator of fraction {i + 1}: "))
    den = int(input(f"Enter the denominator of fraction {i + 1}: "))
    # Append the fraction as a tuple (numerator, denominator) to the list
    fractions.append((num, den))

 

print("The list of fractions is:", fractions)

