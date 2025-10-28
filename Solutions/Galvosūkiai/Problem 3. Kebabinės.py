n = int(input())
arr = list(map(int, input().split()))
while len(arr) < n:
    arr.extend(map(int, input().split()))
visits = [100000] * (2 * 10**5 + 1)
for i, el in enumerate(arr):
    visits[el] = i

min_value = min(visits)
print(visits.index(min_value))
