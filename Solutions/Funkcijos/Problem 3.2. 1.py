def min_max(*arr):
    return min(arr), max(arr)

with open("duom.txt", "r") as fin, open("rez.txt", "w") as fout:
    n = int(fin.readline())
    for i in range(n):
        arr = list(map(int, fin.readline().split()))
        min_val, max_val = min_max(*arr)
        fout.write(f"{min_val} {max_val}\n")