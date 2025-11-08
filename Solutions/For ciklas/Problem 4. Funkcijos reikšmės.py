import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

a, b, c = map(int, input().split())
for x in range(-3, 4):
    y = a * x * x + b * x + c
    print(f"Kai x={x}, tai y={y}")