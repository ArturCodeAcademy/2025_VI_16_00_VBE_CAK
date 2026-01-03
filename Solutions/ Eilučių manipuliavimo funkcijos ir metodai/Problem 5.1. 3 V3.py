import sys
# sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

with open("duom.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = "!?,.;"
for i, c in enumerate(text):
    if c in chars:
        continue
    elif c == " " and i < len(text) - 1 and text[i + 1] in chars:
        print(text[i + 1], end="")
        if i + 1 != len(text) - 2:
            print(" ", end="")
    else:
        print(c, end="")