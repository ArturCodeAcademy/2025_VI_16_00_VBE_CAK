s1, v1, s2, v2 = map(int, input().split())
t1 = s1 * v2
t2 = s2 * v1

if t1 > t2:
    print("Pirmoji didesne")
elif t2 > t1:
    print("Antroji didesne")
else:
    print("Trupmenos lygios")
