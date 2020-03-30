# voca 파일 열기
# 파일 경로는 "vocabulary.txt" 입니다.
from random import randint

dictonary = {}
in_file = open('vocabulary.txt', 'r')

for line in in_file:
    temp = line.strip().split(": ")
    voca_eng = temp[0]
    voca_kor = temp[1]
    dictonary[voca_eng] = voca_kor

# 파일 닫기
in_file.close()
print(dictonary)
print(dictonary.keys())
print(dictonary.values())
dictonary_values = list(dictonary.values())
dictonary_keys = list(dictonary.keys())

print(dictonary_keys)
print(len(dictonary_keys))

# print(x)
# print(dictonary_keys[x])

while True:
    x = randint(0, len(dictonary_keys) - 1)
    voca_kor = dictonary_keys[x]
    voca_eng = dictonary_values[x]
    guess = input("%s: " % voca_kor)

    if guess == 'q' or guess == 'ㅂ':
        break

    # guess = input("%s: " % voca_kor)

    if voca_eng == guess:
        print("맞췄습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % voca_eng)
