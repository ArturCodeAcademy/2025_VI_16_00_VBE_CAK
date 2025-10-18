a1, b1, a2, b2, a3, b3 = map(int, input().split())

S1 = a1 * b1 / 2
S2 = a2 * b2 / 2
S3 = a3 * b3 / 2

if S1 == S2 or S1 == S3 or S2 == S3:
    print("Taip")
else:
    print("Ne")