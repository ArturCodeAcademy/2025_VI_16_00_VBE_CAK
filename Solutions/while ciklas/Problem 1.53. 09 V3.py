n = input()
c = 0

for digit in n:
    if digit in '02468':
        c += 1

print(c)