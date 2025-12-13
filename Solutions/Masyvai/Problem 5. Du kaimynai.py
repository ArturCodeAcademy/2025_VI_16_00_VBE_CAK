import sys
sys.stdin = open("U1.txt", "r", encoding="utf-8")
sys.stdout = open("U1rez.txt", "w", encoding="utf-8")

n = int(input())
arr = list(map(int, input().split()))
print(f"{sum(arr[1:-1]) / (n - 2):.3f}")
