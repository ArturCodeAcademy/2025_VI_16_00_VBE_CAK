with open("rez.txt", "w") as fout:
    for i in range(1, 100):
        fout.write(f"{i * i}\n")