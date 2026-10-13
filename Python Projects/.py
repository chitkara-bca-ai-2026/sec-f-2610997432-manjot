import math

# 1. Take Input—Ask the user to enter two numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2 & 3. Perform calculations
power_res = num1 ** num2
sqrt_res = math.sqrt(num1)
ceil_res = math.ceil(num1 / num2)
floor_res = math.floor(num1 / num2)
abs_diff_res = abs(num1 - num2)
circle_area_res = math.pi * (num1 ** 2)
hypotenuse_res = math.hypot(num1, num2)

# 4. Display all results formatted matching expected output
print(f"{num1} ^ {num2} = {power_res:.1f}" if power_res.is_integer() else f"{num1} ^ {num2} = {power_res:.2f}")
print(f"Square root of {num1} = {sqrt_res:.2f}")
print(f"Ceil of {num1} / {num2} = {ceil_res}")
print(f"Floor of {num1} / {num2} = {floor_res}")
print(f"Absolute difference: {abs_diff_res:.1f}" if abs_diff_res.is_integer() else f"Absolute difference: {abs_diff_res:.2f}")
print(f"Area of circle with radius {num1} = {circle_area_res:.2f}")
print(f"Hypotenuse: {hypotenuse_res:.2f}")


