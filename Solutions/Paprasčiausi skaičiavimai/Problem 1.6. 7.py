n, limit = map(int, input().split())
heights = list(map(int, input().split()))

count = 0
for height in heights:
    if height > limit:
        count += 1

print(count)