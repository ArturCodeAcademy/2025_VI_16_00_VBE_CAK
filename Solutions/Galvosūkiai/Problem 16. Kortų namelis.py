last = 0
for i in range(1, 20):
    n = i
    kortuSk = 0
    while n > 0:
        s = 2 * n + n - 1
        kortuSk += s
        n -= 1
    print(i, "->", kortuSk, " +", kortuSk - last)
    last = kortuSk