import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

n = int(input())
for i in range(1, n + 1, 2):
    if i != 1:
        print(",", end="")
    print(i, end="")

for i in range(2, n + 1, 2):
    print(",", end="")
    print(i, end="")