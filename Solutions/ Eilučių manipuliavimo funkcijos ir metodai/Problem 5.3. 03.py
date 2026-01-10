c = 0
for char in input():
    if char == ' ':
        c += 1
    elif char == '.':
        print(c)
        c = -1