# 2의 n 제곱의 결과값을 출력하는 프로그램
# 2^0 = 1 부터 2^10 = 1024 까지 출력
# 코드를 입력하세요.

for i in range(11):
    # print("2^{} = {}".format(i, 2**i))
    print("2^%d = %d" % (i, 2 ** i))