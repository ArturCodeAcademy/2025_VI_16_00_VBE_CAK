n = int(input())
m = 0
k = 0

while n > 0:
    if n % 2 == 0:
        m += n // 2
        n //= 2
    else:
        m += 1
        n -= 1

    k += 1
    # print(k, n, m)
print(k)