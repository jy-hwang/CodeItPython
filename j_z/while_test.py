i = 2
while i <= 10:
    print(i)
    i = i + 2

j = 100
x = 1
y = 1
while y < 100:
    y = x * 23
    if y > 100:
        print(y)
    x = x + 1

z = 100
# while z 가 100의 배수가 아니다
# z = z + 1

while z % 23 != 0:
    z = z + 1

print(z)
