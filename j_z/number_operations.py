# 덧셈
print(3 + 1.5)
# 뺄셈
print(4.0 - 1)
# 곱셈
print(3.0 * 2.0)
# 거듭제곱
print(2.0 ** 3.0)
# 나누기
print()
# 몫 과 나머지
a = 7
b = 5
print(a // b, a % b)
print(divmod(a, b))
# 버림 나눗셈(floor division)
print(7 / 2)
print(7 // 2)


# round(반올림 : round to nearest even 가까운 짝수를 만들어 줌)

def divide(number1, number2):
    return (number1 // number2), (number1 % number2)


print(divide(10, 2))
