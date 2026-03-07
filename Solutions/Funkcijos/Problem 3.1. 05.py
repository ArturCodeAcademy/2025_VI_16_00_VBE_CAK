class Nums:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.avg = (a + b) / 2

    def __str__(self):
        return f"{self.a:.2f} {self.b:.2f} {self.avg:.2f}"

n = int(input())
for _ in range(n):
    a, b = map(float, input().split())
    nums = Nums(a, b)
    print(nums)