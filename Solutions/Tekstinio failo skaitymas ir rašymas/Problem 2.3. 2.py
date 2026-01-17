a, b, c = 0, 1, 1
n = int(input())
with open("rez.txt", "w") as fout:
    for _ in range(n):
        fout.write(f"{a}\n")
        print(a, b, c)
        a, b, c = b, c, b + c