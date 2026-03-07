class Money:
    def __init__(self, lt, ct):
        self.lt = lt
        self.ct = ct
        self.amount = lt * 100 + ct

    def __str__(self):
        return f"{self.lt} Lt {self.ct} ct"

    def __sub__(self, other):
        total_amount = self.amount - other.amount
        lt = total_amount // 100
        ct = total_amount % 100
        return Money(lt, ct)


with open("duom.txt", "r") as fin, open("rez.txt", "w") as fout:
    n = int(fin.readline())
    for _ in range(n):
        lt, ct, lt2 = map(int, fin.readline().split())
        money1 = Money(lt, ct)
        money2 = Money(lt2, 0)
        result = money2 - money1
        str_rez = str(result)
        fout.write(str_rez + "\n")