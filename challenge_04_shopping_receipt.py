# Collect item names and prices

item1 = input("Enter the name of item 1: ")
price1 = float(input("Enter the price of item 1: "))

item2 = input("Enter the name of item 2: ")
price2 = float(input("Enter the price of item 2: "))

item3 = input("Enter the name of item 3: ")
price3 = float(input("Enter the price of item 3: "))

# Calculate total
total = price1 + price2 + price3

# Print formatted receipt
print("\n------ RECEIPT ------")
print(f"{item1:<20} ${price1:>8.2f}")
print(f"{item2:<20} ${price2:>8.2f}")
print(f"{item3:<20} ${price3:>8.2f}")
print("---------------------")
print(f"{'Total':<20} ${total:>8.2f}")
