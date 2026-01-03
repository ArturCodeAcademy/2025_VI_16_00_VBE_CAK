import sys
# sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

with open("duom.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = "!?,.;"
new_text = ""
for i, c in enumerate(text):
    if c in chars:
        continue
    elif c == " " and i < len(text) - 1 and text[i + 1] in chars:
        new_text += text[i + 1] + " "
    else:
        new_text += c

print(new_text.strip())