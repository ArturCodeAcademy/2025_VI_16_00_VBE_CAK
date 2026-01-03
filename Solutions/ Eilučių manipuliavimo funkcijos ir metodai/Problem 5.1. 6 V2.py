import sys
# sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

with open("duom.txt", "r", encoding="utf-8") as f:
    text = f.read()

lt_alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
text = text.upper()
d = dict()

for c in text:
    if c in lt_alphabet:
        d[c] = d.get(c, 0) + 1

for c in lt_alphabet:
    if c in d:
        print(c, d[c])