from random import randint, uniform

# a <= N <= b 인 랜덤한정수(난수) N 의 값을 리턴시켜준다.
print(randint(1, 20))

# a <= N <= b 인 랜덤한소수(난수) N 의 값을 리턴시켜준다.
print(uniform(0, 1))

x = randint(1, 20)
count = 4
# 상수
# NUM_TRIES = 4
# ANSWER = randint(1,2)

# 변수
# tries = 0
# guess = -1
# while tries < NUM_TRIES and guess != ANSWER
# guess 는 처음에 -1 이고 answer 는 1~20이기때문에 guess != ANSWER 는 처음에 무조건 True 임.
print(x)
while count > 0:
    y = int(input("기회가 %d 번남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % count))
    if x > y:
        print("Up")
        count = count - 1
    elif x < y:
        print("Down")
        count = count - 1
    elif x == y:
        print("축하합니다. %d 번 만에 숫자를 맞추셨습니다." % (5 - count))
        break
    if count == 0:
        print("아쉽습니다. 정답은 %d였습니다." % x)
        break

'''
while tries < NUM_TRIES and guess != ANSWER:
    guess = int(input("기회가 %d 번남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % (NUM_TRIES - tries)))
    tries = tries + 1

    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")

if guess == ANSWER:
    print("축하합니다. %d 번 만에 숫자를 맞추셨습니다." % (tries)
else:
    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))
'''
