with open("u01_duom.txt", "r") as fin:
    lines = fin.readlines()[1:]  # Skip the first line
    values = list(map(int, lines))
    s = sum(values)
    print(s)