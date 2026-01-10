line = input()

if len(line) == 3:
    print(0)
    exit()

sl = sorted("RGB")
if (   sorted(line[:3]) == sl
    or sorted(line[-3:]) == sl):
    print(1)
    exit()

if (   sorted(line[:1] + line[-2:]) == sl
    or sorted(line[:2] + line[-1:]) == sl):
    print(2)
    exit()

for i in range(1, len(line) - 3):
    if sorted(line[i:i+3]) == sl:
        print(2)
        exit()

if line[0] == line[-1]:
    print(4)
    exit()

print(3)