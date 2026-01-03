import sys
# sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

with open("duom.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
count = 0
for word in words:
    if word[0].isupper():
        count += 1

print(count)