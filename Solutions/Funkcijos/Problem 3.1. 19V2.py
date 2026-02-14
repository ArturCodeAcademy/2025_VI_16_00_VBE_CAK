import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(float, input().split())
    x.append(xi)
    y.append(yi)

total_dist = 0
for i in range(n):
    total_dist += dist(x[i], y[i], x[(i + 1) % n], y[(i + 1) % n])

print(f"{total_dist:.3f}")