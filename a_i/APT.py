year = 1988
reward = 50000000
RATE = 12
APT = 1100000000
bank = 0
count = 0
total = 0
while year < 2016:
    reward = reward + RATE / 100 * reward

    count = count + 1
    year = year + 1

# print(reward)

if reward > APT:
    print("{}원 차이로 동일 아저씨의 말씀이 맞습니다.".format(int(reward - APT)))
elif reward < APT:
    print("{}원 차이로 미란 아주머니의 말씀이 맞습니다.".format(int(APT - reward)))
else:
    print("똑같습니다.")

# print("은행에 {}만원을 {}% 로 {}년 맡기면 {}만원 됩니다.".format(reward, RATE*100, count, total))
# 가나다라
