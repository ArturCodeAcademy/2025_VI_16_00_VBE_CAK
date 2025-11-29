n = int(input())
i = 1
while i <= n:
    n -= i
    i += 1

if n == 0:
    print("TAIP")
else:
    print("NE")