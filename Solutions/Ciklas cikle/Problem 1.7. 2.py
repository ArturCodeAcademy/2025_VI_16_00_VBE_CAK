k = int(input())
root = int(k ** 0.5) + 1
for i in range(1, root):
    for j in range(i, root):
        if i ** 2 + j ** 2 == k:
            print("TAIP")
            exit(0)

print("NE")