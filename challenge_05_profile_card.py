# Collect user data

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_m = float(input("Enter your height in metres: "))
fav_number = int(input("Enter your favourite number: "))

# Convert height to centimetres
height_cm = int(height_m * 100)

# Print profile card
print("\n====== PROFILE CARD ======")
print(f"Name:            {name}")
print(f"Age:             {age} years old")
print(f"Height:          {height_m:.2f} m ({height_cm} cm)")
print(f"Favourite Number: {fav_number}")
print("==========================")
