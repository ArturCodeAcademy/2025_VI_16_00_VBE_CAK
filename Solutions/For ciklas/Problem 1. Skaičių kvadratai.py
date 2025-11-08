import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

a, n = map(int, input().split())
for i in range(a, n + 1):
    print(i * i)
