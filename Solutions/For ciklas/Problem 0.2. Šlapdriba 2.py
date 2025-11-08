import sys
sys.stdin = open('U1.txt', 'r', encoding='utf-8')
sys.stdout = open('U1rez.txt', 'w', encoding='utf-8')

n = int(input())
for i in range(n):
    print(i + 1, end=" ")
    if i % 2 != 0:
        print("**")
    else:
        print("*0")