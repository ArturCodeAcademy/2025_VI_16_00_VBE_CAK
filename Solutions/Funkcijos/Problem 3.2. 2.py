class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.S = a * b
        self.P = 2 * (a + b)

    def __str__(self):
        return f"{self.a} {self.b} {self.S} {self.P}"

with open("duom.txt", "r") as fin, open("rez.txt", "w") as fout:
    n = int(fin.readline())
    for _ in range(n):
        a, b = map(int, fin.readline().split())
        rect = Rect(a, b)
        str_rez = str(rect)
        fout.write(str_rez + "\n")