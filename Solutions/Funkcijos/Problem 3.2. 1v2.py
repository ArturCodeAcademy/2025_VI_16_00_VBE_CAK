def min_max(a, b, c):
    mn = a
    mx = a
    if b < mn:
        mn = b
    if c < mn:
        mn = c
    if b > mx:
        mx = b
    if c > mx:
        mx = c
    return mn, mx

with open("duom.txt", "r") as fin, open("rez.txt", "w") as fout:
    n = int(fin.readline())
    for i in range(n):
        a, b, c = map(int, fin.readline().split())
        min_val, max_val = min_max(a, b, c)
        fout.write(f"{min_val} {max_val}\n")