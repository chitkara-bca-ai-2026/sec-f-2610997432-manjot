"""
Lab 07 - Calendar Verification System
File name: lab07_calendar_verification.py
"""

def verify_calendar():
    print("========================================")
    print("      CALENDAR VERIFICATION SYSTEM      ")
    print("========================================")
    
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("Error: Please enter a valid integer for the year.")
        return

    print("========================================")
    if year <= 0:
        print("Error: The year must be a positive integer greater than 0.")
        return

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
            reason = "Not divisible by 4 (Common year)"

    print(f"Year: {year}")
    
    if is_leap:
        print("Status: LEAP YEAR")
        print("Days in Year: 366 days")
        print("Days in February: 29 days")
    else:
        print("Status: COMMON YEAR")
        print("Days in Year: 365 days")
        print("Days in February: 28 days")
        
    print(f"Reason: {reason}")
    print("========================================")

if __name__ == "__main__":
    verify_calendar()
