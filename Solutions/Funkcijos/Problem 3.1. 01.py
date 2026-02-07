def average(a, b, c):
    return (a + b + c) / 3

a, b, c = map(float, input().split())
avg = average(a, b, c)
print(f"{avg:.2f}")