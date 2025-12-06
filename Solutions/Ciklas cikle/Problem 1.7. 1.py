k = int(input())
a = k // 3
while True:
    b = 0
    while a * 3 - b * 5 >= k:
        if (a * 3 - b * 5) == k:
            print(f"Alisa - {a}, Bazilijus - {b}")
            exit(0)
        b += 1
    a += 1
