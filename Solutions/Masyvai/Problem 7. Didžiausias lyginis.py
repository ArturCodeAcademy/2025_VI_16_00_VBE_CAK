import sys
#sys.stdin = open("U1.txt", "r")
#sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
index = -1
for i, el in enumerate(arr):
    if el % 2 != 0:
        continue

    if index == -1 or el > arr[index]:
        index = i

if index != -1:
    print(arr[index])
else:
    print("Ne")