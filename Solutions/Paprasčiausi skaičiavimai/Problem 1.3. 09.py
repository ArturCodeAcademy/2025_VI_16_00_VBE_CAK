# TC=5 (TF−32)/9.
# TC * 9/5 + 32 = TF
tc = float(input())
tf = tc * 9 / 5 + 32
if tf % 1 == 0:
    print(int(tf))
else:
    print(tf)