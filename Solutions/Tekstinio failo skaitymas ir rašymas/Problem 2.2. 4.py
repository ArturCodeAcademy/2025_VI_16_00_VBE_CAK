with open("u05_duom.txt", "r") as fin:
    text = fin.read()
    values = list(map(int, text.split()[1:]))

count = 0
for i, value in enumerate(values):
    if i == 0:
        continue
    if value < values[i - 1]:
        count += 1

print(count)
