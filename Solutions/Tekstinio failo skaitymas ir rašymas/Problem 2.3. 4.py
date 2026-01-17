import math

n = int(input())
with open("rez.txt", "w") as fout:
    fout.write("+––––––+––––––+––––––+\n")
    fout.write("|   a  |   b  |   c  |\n")
    fout.write("+––––––+––––––+––––––+\n")
    for i in range(5, n + 1):
        c = i
        b = c - 1
        a = int(math.sqrt(c * c - b * b))
        if a * a + b * b == c * c:
            fout.write(f"|{a:5} |{b:5} |{c:5} |\n")
    fout.write("+––––––+––––––+––––––+\n")
