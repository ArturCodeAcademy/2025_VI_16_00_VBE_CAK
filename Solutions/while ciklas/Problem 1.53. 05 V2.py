n = int(input())
i = 1
while True:
    if n <= 0:
        break
    n -= i
    i += 1

if n == 0:
    print("TAIP")
else:
    print("NE")