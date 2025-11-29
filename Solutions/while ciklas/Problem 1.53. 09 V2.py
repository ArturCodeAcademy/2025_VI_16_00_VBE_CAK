n = input()
c = 0

for digit in n:
    if int(digit) % 2 == 0:
        c += 1

print(c)