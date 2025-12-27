import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
max_value = None
for i in range(n):
    if arr.count(arr[i]) > 1:
        continue

    if max_value is None or max_value < arr[i]:
        max_value = arr[i]


if max_value is not None:
    print(max_value)
else:
    print("NO")
