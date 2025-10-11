import math


r1, r2 = map(float, input().split())
area_diff = math.pi * (r1**2 - r2**2)
print(round(area_diff), "kv. mm")