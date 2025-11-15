import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

n = int(input())
for n in range(1, 100):
    count = 0
    even_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
            count += 1

    print(n, end=': ')
    if count == 0:
        print("NO")
    else:
        print(even_sum // count)