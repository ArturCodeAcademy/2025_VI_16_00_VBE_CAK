v1 = True
v2 = False
for i in range(1, 11):
    for j in range(1, 11):
        if v1:
            print(f"{i * j:4}", end="")
        elif v2:
            num_as_str = str(i * j)
            digits = len(num_as_str)
            print(" " * (4 - digits), end=num_as_str)
        else:
            num = i * j
            if num < 10:
                print(f"   {num}", end="")
            elif num < 100:
                print(f"  {num}", end="")
            else:
                print(f" {num}", end="")

    print()
