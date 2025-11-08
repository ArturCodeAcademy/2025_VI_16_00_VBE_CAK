import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)