with open("u01_duom.txt", "r") as fin:
    text = fin.read()
    values = list(map(int, text.split()[1:]))
    s = sum(values)
    print(s)