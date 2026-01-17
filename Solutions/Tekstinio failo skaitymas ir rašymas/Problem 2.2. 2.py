with open("u02_duom.txt", "r") as fin:
    text = fin.read()
    values = list(map(int, text.split()[1:]))

for value in values:
    if value < 0:
        print("TAIP")
        break
else:
    print("NE")