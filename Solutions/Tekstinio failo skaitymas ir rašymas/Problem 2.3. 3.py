input()
values = list(map(int, input().split()))
with open("rez.txt", "w") as fout:
    for value in values:
        if value == 0:
            fout.write("1\n")
        elif value < 0:
            fout.write(f"{value * value}\n")
        else:
            fout.write(f"{value}\n")
