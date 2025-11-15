import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

a, b = map(int, input().split())
count = 0
for i in range(10, 100):
    if i % a == 0 and i % b == 0:
        print(i)
        count += 1

if count == 0:
    print("NERA")