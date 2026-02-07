# sudėtį - 1, atimtį - 2, daugybą - 3, dalmens radimą - 4, liekanos radimą - 5
def calculate(a, b, operation):
    if operation == 1:
        return a + b
    elif operation == 2:
        return a - b
    elif operation == 3:
        return a * b
    elif operation == 4:
        return a // b
    else:
        return a % b

n = int(input())
for _ in range(n):
    a, b, operation = map(int, input().split())
    print(calculate(a, b, operation))

