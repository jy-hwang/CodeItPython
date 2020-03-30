i = 1
j = 120
count = 0
while i <= j:
    if (j % i == 0):
        print(i)
        count = count + 1
    i = i + 1
print("{}의 약수는 총 {}개입니다.".format(j, count))
