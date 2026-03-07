class Nums:
    def __init__(self, a, b, c):
        self.max_val = max(a, b, c)
        self.min_val = min(a, b, c)

    def __str__(self):
        return f"{self.min_val} {self.max_val}"

with open("duom.txt", "r") as fin, open("rez.txt", "w") as fout:
    n = int(fin.readline())
    for _ in range(n):
        a, b, c = map(int, fin.readline().split())
        nums = Nums(a, b, c)
        str_rez = str(nums)
        fout.write(str_rez + "\n")