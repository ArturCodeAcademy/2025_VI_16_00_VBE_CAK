def dbd(a, b):
    ans = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

def mbk(a, b):
    return a * b // dbd(a, b)

input()
arr = list(map(int, input().split()))

ans = arr[0]
for i in range(1, len(arr)):
    ans = mbk(ans, arr[i])

print(ans)