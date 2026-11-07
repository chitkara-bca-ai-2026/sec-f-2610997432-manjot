#def check_even_odd(n):
  #if n % 2 == 0:
    #return 'EVEN'
  #else:
    #return 'ODD'

#def c_to_f(celsius):
  #f = (celsius * 9 / 5) + 32
  #return f


#n= int(input())
#temp_c = float(input())
#print(f'Number is: {check_even_odd(n)}')
#print(f'Fahrenheit: {c_to_f(temp_c):.2f}')
#def total_cost(price, quantity):
  #return price * quantity
#price = float(input())
#quantity = int(input())
#print(f'Total cost: {total_cost(price, quantity):.2f}')
# 'tax' has a default argument (0.05)
def calculate_bill(price, tax=0.05):
  total = price + (price * tax)
  return total  # Returns the result to be saved


# 1. Positional argument call
bill1 = calculate_bill(100)
print('Bill 1:', bill1)  # Output: 105.0

# 2. Keyword argument call (order doesn't matter)
bill2 = calculate_bill(price=200, tax=0.10)
print('Bill 2:', bill2)  # Output: 220.0
