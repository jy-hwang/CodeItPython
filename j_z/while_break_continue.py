i = 100
while True:
    if i % 23 == 0:
        break
    i = i + 1
print(i)

j = 0
while j < 15:
    j = j + 1

    if j % 2 == 1:
        continue
    print(j)
