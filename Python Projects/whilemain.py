num = 2 

while num <= 10:
    print(num)
    num += 2  
num = 1

while num <= 10:def main():
    print("========================================")
    print("       CALENDAR VERIFICATION SYSTEM     ")
    print("========================================")
    
    # 1. Take Input from the user
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("\nInvalid input! Please enter a valid integer.")
        return

    # 2. Validate the input
    if year <= 0:
        print("\nError: Year must be a positive integer greater than 0.")
        return

    # 3. Check leap year rules using if-else
    is_leap = False
    reason = ""

    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
            reason = "Century year divisible by 400"
        else:
            is_leap = False
            reason = "Century year not divisible by 400"
    else:
        if year % 4 == 0:
            is_leap = True
            reason = "Divisible by 4 and not a century year"
        else:
            is_leap = False
            reason = "Not divisible by 4"

    # 4. Determine calendar details
    if is_leap:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_february = 29
    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_february = 28

    # 5. Display the results clearly
    print("----------------------------------------")
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {days_in_year} days")
    print(f"Days in February: {days_in_february} days")
    print(f"Reason: {reason}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()

    if num % 2 == 0: 
        print(num)
    num += 1  
glass = 3  

while glass > 0:
    print("Taking a sip...")
    glass= glass-1

print("Glass is empty!")
num = 0

while num < 5:
    num += 1
    
    if num == 3:
        continue  
        
    print(num)
    c = 0
    while c <=3:
        print("Checking door", c)
        c+= 1
else:                                           
        print("checked all doors! ")
count = 1
while count <= 5:
     if count == 3:
          print("found key  at door 3")
          break
     count += 1
else:
        print("checked all doors! ")
        num = 7
while num <= 3:
    print(num)
    num += 1
else:
    print("Loop finished normally!")
c= 1
while c <= 5:
    print(c)
    c += 1
else:
    print("Loop finished normally!")
    
         # Step 1: Ask user for input
num = int(input("Enter a number (1 to 20): "))

# Step 2: Validate input
if num < 1 or num > 20:
    print("Invalid input! Please enter a number between 1 and 20.")
else:
    print(f"\nMultiplication Table of {num}")
    print("**************************")
    
    # Initialize variables for while loop
    i = 1
    total_sum = 0
    
    # Step 3: Print table using a while loop
    while i <= 10:
        result = num * i
        print(f"{num} x {i} = {result}")
        total_sum += result
        i += 1
    
    print("**************************")
    
    # Step 4: Display smallest result, largest result, and sum
    smallest = num * 1
    largest = num * 10
    
    print(f"Smallest result: {smallest}")
    print(f"Largest result: {largest}")
    print(f"Sum of all results: {total_sum}")
apples = ["apple 1", "apple 2", "apple 3"]

for apple in apples:
    print("Put sticker on", apple)

