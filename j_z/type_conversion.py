# 형 변환 type_conversion or type_casting

print(int(3.141592))
print(float(3))

print(int("2") + int("5"))

print(type(str(2) + str(5)))

age = 10

print("제 나이는 " + str(age) + "살 입니다.")

# 오늘은 2020년 3월 19일 입니다.
year = 2020
month = 3
day = 19

print("오늘은 " + str(year) + "년 " + str(month) + " 월" + str(day) + "일 입니다.")
# print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day))

like_string = "저는 {},{},{} 을/를 좋아합니다."
print(like_string.format("펭수", "페이커", "세종대왕"))
