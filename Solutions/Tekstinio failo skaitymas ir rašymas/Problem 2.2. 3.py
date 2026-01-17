with open("u03_duom.txt", "r") as fin:
    text = fin.read()
    values = list(map(int, text.split()[1:]))

count = 0
for value in values:
    if abs(value) % 2 != 0:
        count += 1

print(count)
