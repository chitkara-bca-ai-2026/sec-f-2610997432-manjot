a = input('Enter Tuition fee: ')
b = input('Enter Lab fee: ')
c = input('Enter Library fee: ')
d = input('Enter Exam fee: ')
e = input('Enter Discount amount: ')
print('Tuition fee:', a)
print('Lab fee:', b)
print('Library fee:', c)
print('Exam fee:', d)
add = int(a) + int(b) + int(c) + int(d)
print('Total fee:', add)
sub = add - int(e)
print('Fee after discount:', sub)
multiply = sub * 2
print('Annual fee:', multiply)
divide = multiply / 12
print('Monthly Installment:', divide)

