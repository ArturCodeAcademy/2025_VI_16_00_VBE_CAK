a, b, c, d = map(int, input().split())

if a == b == c:
    print("Ketvirtasis")
elif a == b == d:
    print("Treciasis")
elif a == c == d:
    print("Antrasis")
elif b == c == d:
    print("Pirmasis")

if a == b:
    if a == c:
        print("Ketvirtasis")
    else:
        print("Treciasis")
else:
    if a == c:
        print("Antrasis")
    else:
        print("Pirmasis")
