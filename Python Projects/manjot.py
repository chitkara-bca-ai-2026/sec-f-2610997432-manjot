number = 5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
marks = 32
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    signal = "green"
if signal == "red":
    print("Stop!")
elif signal == "yellow":
    print("Slow down!")
else:
    print("Go!")
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You can't vote")
    print(f"Wait for {18 - age} yrs")
