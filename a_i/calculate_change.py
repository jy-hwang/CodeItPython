def calculate_change(payment, cost):
    # 코드를 작성하세요.

    FIFTY_THOUSAND = 50000
    TEN_THOUSAND = 10000
    FIVE_THOUSAND = 5000
    ONE_THOUSAND = 1000

    fifty_count = 0
    ten_count = 0
    five_count = 0
    one_count = 0
    rest = 0
    change = payment - cost
    while True:
        if change > FIFTY_THOUSAND:
            fifty_count = change // FIFTY_THOUSAND
            change = change % FIFTY_THOUSAND
            break
        elif change > TEN_THOUSAND:
            ten_count = change // TEN_THOUSAND
            change = change % TEN_THOUSAND
            break
        elif change > FIVE_THOUSAND:
            five_count = change // FIVE_THOUSAND
            change = change % FIVE_THOUSAND
            break
        elif change > ONE_THOUSAND:
            one_count = change // ONE_THOUSAND
            change = change % ONE_THOUSAND
            break
        else:
            return False
    print("{}원 지폐 : {}장".format(FIFTY_THOUSAND, fifty_count))
    print("{}원 지폐 : {}장".format(TEN_THOUSAND, ten_count))
    print("{}원 지폐 : {}장".format(FIVE_THOUSAND, five_count))
    print("{}원 지폐 : {}장".format(ONE_THOUSAND, one_count))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
