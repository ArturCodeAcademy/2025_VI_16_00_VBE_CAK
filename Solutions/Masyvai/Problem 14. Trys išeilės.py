import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
exists = False
for i in range(n - 2):
    if arr[i] + 1 == arr[i + 1] and arr[i] + 2 == arr[i + 2]:
        exists = True
        break

if exists:
    print("TAIP")
else:
    print("NE")