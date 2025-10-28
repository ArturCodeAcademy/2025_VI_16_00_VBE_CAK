m1, s1, m2, s2 = map(float, input().split())
k1 = s1 / m1
k2 = s2 / m2

if k1 > k2:
    print("Riesutiniai brangesni")
elif k1 < k2:
    print("Karameliniai brangesni")
else:
    print("Abieju kainos vienodos")