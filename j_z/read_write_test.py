# 매출 파일 열기
# 파일 경로는 "data/chicken.txt" 입니다.

in_file = open('data/chicken.txt', 'r', encoding='utf8')
count = 0
sum = 0
for line in in_file:
    temp = line.strip().split(": ")
    sum += int(temp[1])
    count += 1

print(sum / count)
# 만약 count 없이 31로 나눌경우, 이를 하드코딩했다고 표현한다.
#

# 파일 닫기
in_file.close()
