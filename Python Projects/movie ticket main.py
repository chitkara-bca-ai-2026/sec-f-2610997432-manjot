age= int(input())
day = input()
if age<12:
    price = 120
elif age>12 and age<=59:
    price = 250
else: 
    price = 150
if day == 'W':
    price = (price-50)
print ('Ticket Price = ', price)

