import sys
# sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

with open("duom.txt", "r", encoding="utf-8") as f:
    text = f.read()

lt_alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
text = text.upper()

for c in lt_alphabet:
    count = text.count(c)
    if count > 0:
        print(c, count)