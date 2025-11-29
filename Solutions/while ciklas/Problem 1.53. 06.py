a, b, c = map(int, input().split())
n = 1

while True:
    if c < a:
        break
    a += b
    n += 1

print(n)