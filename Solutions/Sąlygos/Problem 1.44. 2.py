s0, v1, v2, t = map(int, input().split())

s1 = v1 * t
s2 = v2 * t

dist = s0 + s1 - s2

if v1 >= v2:
    print(dist, "km. Niekada nepavys")
elif v1 < v2 and dist > 0:
    print(dist, "km. Pavys")
elif dist == 0:
    print("0 km. Pasivijo")
else:
    print(-dist, "km. Aplenke")