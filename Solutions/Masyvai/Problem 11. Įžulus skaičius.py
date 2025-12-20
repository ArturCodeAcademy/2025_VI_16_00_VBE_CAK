import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
found = False
element = 0

for i, el in enumerate(arr):
    if el < 0:
        continue

    bigger = False
    if (       i == 0 and el > arr[1]
            or i == n - 1 and el > arr[-2]
            or arr[i - 1] < el > arr[i + 1]):
        if found and el < element or not found:
            element = el
        found = True

if found:
    print(element)
else:
    print("NO")
