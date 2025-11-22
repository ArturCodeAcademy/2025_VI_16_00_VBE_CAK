p, k, s = map(int, input().split())
pk = 0

while s >= p:
    s -= p
    pk += 1
    p += k

print("Pirkejo nupirktu prekiu kiekis:", pk)
