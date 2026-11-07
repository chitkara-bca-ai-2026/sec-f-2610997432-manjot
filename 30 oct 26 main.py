with open('notes.txt', 'w') as f:
    f.write('Python\nJava\nC++')
with open('notes.txt', 'r') as f:
    data = f.read()
    print('Type:', type(data))
    print(data)
with open('notes.txt', 'r') as f:
    print('First 6:', f.read(6))
    print('Next 5 :', repr(f.read(5)))

with open('students.txt', 'w') as f:
    f.write('Aman\nRiya\nKaran\nNeha')
with open('students.txt', 'r') as f:
    for num, line in enumerate(f, 1):
        clean_name = line.strip()
        print(f'Student {num}: {clean_name}')
