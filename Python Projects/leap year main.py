def main():
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
