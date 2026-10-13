ss = "I love java and java is great"
s1 = ss.replace("java", "python")
s1 = s1.split(" ")  
s2 = "|".join(s1)
print(s2)
print('starvy'.isalpha())
print('1234'.isdigit())
print('hello456'.isalnum())
print('hello'.isupper())
print('hello'.islower())
print('  '.isspace())
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

