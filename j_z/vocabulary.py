# 파일 열기
out_file = open('vocabulary.txt', 'w')

while True:
    voca_eng = input("영어 단어를 입력하세요: ")
    if voca_eng == 'q':
        break
    voca_kor = input("한국어 뜻을 입력하세요: ")

    if voca_kor == 'q':
        break
    # 파일에쓰기
    out_file.write("%s: %s\n" % (voca_eng, voca_kor))

# 파일 닫기
out_file.close()
