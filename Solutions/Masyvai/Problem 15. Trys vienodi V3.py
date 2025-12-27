import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if arr.count(arr[i]) > 2:
        print("TAIP")
        exit()

print("NE")
