import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n - 1):
    if arr[i + 1] == arr[i]:
        print("NE")
        exit()

print("TAIP")