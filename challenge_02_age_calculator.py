# Ask the user for their birth year
birth_year = input("Enter your birth year: ")

# Convert the string to an integer
birth_year = int(birth_year)

# Set the current year
current_year = 2026

# Calculate the age
age = current_year - birth_year

# Print the age using an f-string
print(f"You are {age} years old.")

