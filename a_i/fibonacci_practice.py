previous = 0
current = 1
temp = 0
i = 0
count = 20
while i < count:
    temp = current + previous
    print(current)
    previous = current
    current = temp
    i = i + 1
