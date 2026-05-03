g = z = r = 0
with open("U1.txt", "r") as f:
    f.readline()
    for line in f:
        color, value = line.split()
        if line[0] == "G":
            g += int(value)
        elif line[0] == "Z":
            z += int(value)
        elif line[0] == "R":
            r += int(value)

result = min(g, z, r) // 2

with open("U1rez.txt", "w") as f:
    f.write(f"{result}\n")
    f.write(f"G = {g - result * 2}\n")
    f.write(f"Z = {z - result * 2}\n")
    f.write(f"R = {r - result * 2}\n")