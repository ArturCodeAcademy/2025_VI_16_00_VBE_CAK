def num_sort(n):
    s = 0
    while n > 0:
        s *= 10
        s += n % 10
        n //= 10
    return s


def num_sort2(n):
    return int(str(n)[::-1])

input()
arr = list(map(int, input().split()))
for a in arr:
    print(f"{a} {num_sort2(a)}")