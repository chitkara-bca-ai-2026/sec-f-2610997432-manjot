num = 1234  

sum = 0
reversed = 0

while num > 0:
    dig = num % 10
    sum = sum + dig
    reversed = reversed * 10 + dig
    num = num // 10

print(reversed)
