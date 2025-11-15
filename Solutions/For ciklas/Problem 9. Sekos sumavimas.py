import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

n = int(input())
s = 0
for i in range(1, n + 1):
    result = i * (i * 2 - 1)
    s += result
print(s)
