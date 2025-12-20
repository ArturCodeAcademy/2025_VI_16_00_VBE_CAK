import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
arr = list(map(int, input().split()))
a, b, c, *rest = arr

if a % 2 + b % 2 + c % 2 < 2:
    print("NELYGINIS")
else:
    print("LYGINIS")