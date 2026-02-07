def R(r1, r2):
    return (r1 * r2) / (r1 + r2)

r1, r2 = map(float, input().split())
result = R(r1, r2)
print(f"{result:.2f}")