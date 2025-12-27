import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = sorted(map(int, input().split()))
count = 1
last = arr[0]
for i in range(1, n):
    if arr[i] == last:
        count += 1
    else:
        last = arr[i]
        count = 1

    if count >= 3:
        break

if count >= 3:
    print("TAIP")
else:
    print("NE")