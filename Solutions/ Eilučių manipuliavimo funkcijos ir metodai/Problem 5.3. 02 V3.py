text = input()
plus = 0
minus = 0
multiply = 0
divide = 0
for char in text:
    if char == '+':
        plus += 1
    elif char == '-':
        minus += 1
    elif char == '*':
        multiply += 1
    elif char == '/':
        divide += 1
print('+', plus)
print('-', minus)
print('*', multiply)
print('/', divide)