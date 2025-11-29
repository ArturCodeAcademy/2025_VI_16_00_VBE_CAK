a, b, c = map(int, input().split())
n = 1

for _ in range(c // b + 2):
    if c < a:
        break
    a += b
    n += 1

print(n)