n = int(input())
s = 0
for i in range(1, n + 1):
    d = 1
    for j in range(i, i * 2 + 1):
        d *= j
    s += d
print(s)