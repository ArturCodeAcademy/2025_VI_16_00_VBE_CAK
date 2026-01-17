fin = open("u01_duom.txt", "r")

n = int(fin.readline())
s = 0
for i in range(n):
    value = int(fin.readline())
    s += value

fin.close()
print(s)