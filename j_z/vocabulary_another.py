# voca 파일 열기
# 파일 경로는 "vocabulary.txt" 입니다.

in_file = open('vocabulary.txt', 'r')

for line in in_file:
    temp = line.strip().split(": ")
    voca_eng = temp[0]
    voca_kor = temp[1]
    guess = input("%s: " % voca_kor)
    if voca_eng == guess:
        print("맞췄습니다")
    else:
        print("아쉽습니다. 정답은 %s입니다." % voca_eng)

# 파일 닫기
in_file.close()
