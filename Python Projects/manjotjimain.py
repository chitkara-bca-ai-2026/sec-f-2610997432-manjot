# 1. Take Input - Ask the user for details
item_name = input("Enter item name: ")
price = float(input("Enter price per unit: "))
quantity = int(input("Enter quantity: "))

# 2. Calculate subtotal
subtotal = price * quantity

# 3. Apply discount based on the subtotal
if subtotal > 5000:
    discount_percent = 20
elif subtotal > 2000:
    discount_percent = 10
elif subtotal > 1000:
    discount_percent = 5
else:
    discount_percent = 0

# 4. Calculate discount amount and final amount
discount_amount = (discount_percent / 100) * subtotal
final_amount = subtotal - discount_amount

# 5. Print the bill showing all details
print(f"\nItem: {item_name}")
print(f"Price per unit: {price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_percent} %")
print(f"Discount amount: {discount_amount}")
print(f"Final amount: {final_amount}")
