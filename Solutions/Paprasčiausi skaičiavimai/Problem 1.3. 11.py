s0, v1, v2, t = map(float, input().split())
s = round(abs(s0 - (v1 + v2) * t), 6)
if s % 1 == 0:
    print(int(s), "km")
else:
    print(s, "km")