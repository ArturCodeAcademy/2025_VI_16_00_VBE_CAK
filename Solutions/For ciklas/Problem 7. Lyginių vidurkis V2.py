import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

n = int(input())
if n == 1:
    print("NO")
else:
    print(n // 2 + 1)