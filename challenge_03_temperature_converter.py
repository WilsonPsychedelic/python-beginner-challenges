# Ask the user for a temperature in Celsius
celsius = input("Enter temperature in Celsius: ")

# Convert the string input to a float
celsius = float(celsius)

# Apply the conversion formula
fahrenheit = (celsius * 9/5) + 32

# Print the result rounded to 2 decimal places
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

