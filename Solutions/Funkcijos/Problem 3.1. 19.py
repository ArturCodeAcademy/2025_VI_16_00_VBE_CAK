import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

n = int(input())
x1, y1 = map(float, input().split())
x0, y0 = x1, y1
total_dist = 0.0
for i in range(1, n):
    x2, y2 = map(float, input().split())
    total_dist += dist(x1, y1, x2, y2)
    x1, y1 = x2, y2
total_dist += dist(x1, y1, x0, y0)

print(f"{total_dist:.3f}")