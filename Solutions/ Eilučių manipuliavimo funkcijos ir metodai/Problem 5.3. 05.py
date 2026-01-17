# ND Problem 5.3. 05 and start files
line = input()
opened = 0
for ch in line:
    if ch == '(':
        opened += 1
    elif ch == ')':
        opened -= 1

    if opened < 0:
        break



if opened == 0:
    print("TAIP")
else:
    print("NE")