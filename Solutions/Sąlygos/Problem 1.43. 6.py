import math

a, d = map(int, input().split())
if math.sqrt(2 * a ** 2) <= d:
    print("Telpa")
else:
    print("Netelpa")