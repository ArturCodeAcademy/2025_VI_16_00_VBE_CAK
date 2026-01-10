import sys
sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

a, op, b = input().split()
a = int(a)
b = int(b)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if a % b == 0:
        print(a // b)
    else:
        print(f"{a // b} ({a % b} liek.)")