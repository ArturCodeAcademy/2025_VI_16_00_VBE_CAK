import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
unique = True
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            unique = False
            break

    if not unique:
        break

if unique:
    print("TAIP")
else:
    print("NE")
