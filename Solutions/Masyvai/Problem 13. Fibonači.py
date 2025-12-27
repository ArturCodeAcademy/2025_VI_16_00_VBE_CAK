import sys
sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
fibonacci = [0, 1]
for i in range(n - 1):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci[n])