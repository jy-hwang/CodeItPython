# 앞자리 (1단부터 9단까지)
for i in range(1, 10):
    # 뒷자리
    for j in range(1, 10):
        # print("{} * {} = {}".format(i, j, i*j))
        print("%d * %d = %d" % (i, j, i * j))
