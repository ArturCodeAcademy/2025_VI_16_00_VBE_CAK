import sys
sys.stdin = open("duom.txt", "r", encoding="utf-8")
sys.stdout = open("rez.txt", "w", encoding="utf-8")

n = int(input())
input()
queue = input()

#  Mažylis - 2
#  Karlsonas - 5
#  Frekenbok - 3

for p in queue:
    if p == "M":
        r = 2
    elif p == "K":
        r = 5
    else:
        r = 3

    if n > r:
        n -= r
    else:
        if p == "M":
            name = "Mažylis"
        elif p == "K":
            name = "Karlsonas"
        else:
            name = "Frekenbok"

        print(n, name)
        break
else:
    print(n, "liko")
