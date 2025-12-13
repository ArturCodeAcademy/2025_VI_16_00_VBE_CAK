import sys
sys.stdin = open("U1.txt", "r", encoding="utf-8")
sys.stdout = open("U1rez.txt", "w", encoding="utf-8")

n = int(input())
arr = list(map(int, input().split()))
count = 0
s = 0
for i in range(n):
    if arr[i] > 0:
        s += arr[i]
        count += 1

if count > 0:
    print(f"{s / count:.2f}")
else:
    print("NO")
