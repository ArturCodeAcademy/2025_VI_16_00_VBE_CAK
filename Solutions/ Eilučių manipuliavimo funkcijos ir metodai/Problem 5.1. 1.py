import sys
# sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

with open("duom.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text.count("\n"))