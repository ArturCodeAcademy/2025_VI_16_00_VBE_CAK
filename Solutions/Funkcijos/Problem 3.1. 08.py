def num_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def num_sum2(n):
    return sum(map(int, str(n)))


def num_sum3(n):
    str_num = str(n)
    s = 0
    for c in str_num:
        s += int(c)
    return s

input()
arr = list(map(int, input().split()))
for a in arr:
    print(f"{a} {num_sum(a)}")