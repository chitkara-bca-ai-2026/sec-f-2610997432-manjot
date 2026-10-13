# Ask user for input
num = int(input("Enter a number (1 to 20): "))

# Validate input
if num < 1 or num > 20:
    print("Invalid input! Please enter a number between 1 and 20.")
else:
    print(f"\nMultiplication Table of {num}")
    print("**************************")
    
    # Initialize variables
    i = 1
    total_sum = 0
    
    # Print table using a while loop
    while i <= 10:
        result = num * i
        print(f"{num} x {i} = {result}")
        total_sum += result
        i += 1
    
    print("**************************")
    
    # Summary results
    smallest = num * 1
    largest = num * 10
    
    print(f"Smallest result: {smallest}")
    print(f"Largest result: {largest}")
    print(f"Sum of all results: {total_sum}")
