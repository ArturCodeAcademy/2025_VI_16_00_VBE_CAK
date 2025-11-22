n = int(input())
count = 0
total = 0

while n != 0:
    if n > 100:
        count += 1
    total += n
    n = int(input())

print("Zuvu mase:", total)
print("Rimtu zuvu kiekis:", count)