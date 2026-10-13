# Read the 3-digit input PIN as a string
pin = input("Enter a 3-digit PIN: ")

# Extract digits
first_digit = int(pin[0])
middle_digit = int(pin[1])
last_digit = int(pin[2])

# Check security rule
if first_digit + last_digit == middle_digit:
    print("VALID CODE")
else:
    print("INVALID CODE")
