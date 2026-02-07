def volume(a):
    return a ** 3


with open("duom.txt", "r") as fin:
    n = int(fin.readline())
    arr = list(map(float, fin.readline().split()))

with open("rez.txt", "w") as fout:
    for a in arr:
        fout.write(f"{a:.2f} {volume(a):.2f}\n")