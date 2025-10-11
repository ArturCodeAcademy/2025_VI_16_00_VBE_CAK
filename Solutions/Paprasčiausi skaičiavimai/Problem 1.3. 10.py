import math


m, s = map(float, input().split())
p = s / m / 10
lt = int(p)
ct = int(math.floor((p - lt) * 100))

print(lt, "Lt", ct, "ct")