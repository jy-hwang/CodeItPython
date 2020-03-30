# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
# 코드를 입력하세요
i = 1
while i <= 10:
    numbers.append(i)
    i = i + 1
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
'''
j = 0
while j < len(numbers):
    if numbers[j] % 2 == 1 :
        del numbers[j]
    j = j + 1
'''
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 == 1:
        del numbers[i]
    i = i - 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)

print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
# numbers.sort()
print(sorted(numbers))
