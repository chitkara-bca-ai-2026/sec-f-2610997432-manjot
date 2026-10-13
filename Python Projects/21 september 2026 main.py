first = 'hello'
last = 'world'
print(first + ' ' + last)
# --- Concatenation (+) ---
first = "Hello"
last = "World"

# Joining strings with a space in between
full = first + " " + last
print("Concatenation example:")
print(full)  # Output: Hello World
print()

# --- Repetition (*) ---
# Repeating a single character or word
dash = "-" * 30
laugh = "ha" * 3

print("Repetition examples:")
print(dash)   # Output: ------------------------------
print(laugh)  # Output: hahaha
print()

# --- Type Conversion (str) ---
# Adding a number to a string directly causes a TypeError:
# "Age: " + 20  <-- This would raise TypeError!

# Correct way: convert the number to a string first using str()
age = 20
result = "Age: " + str(age)

print("Type conversion example:")
print(result) # Output: Age: 20
a = 'ustaad'
print (a.lower())
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

inverted_triangle(5)
a = 'ustaad'
print(a.upper())
b = 'USTAAD'    
print(b.lower())
c = 'ustaad'
print(c.capitalize())

name = ''
while name.lstrip()== '':
    name = input("Enter your name: ")
print("Name received:", name)