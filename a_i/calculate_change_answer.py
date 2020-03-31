def calculate_change(payment, cost):
    # 코드를 작성하세요.
    change = payment - cost

    fifty_count = change // 50000
    change = change % 50000

    ten_count = change // 10000
    change = change % 10000

    five_count = change // 5000
    change = change % 5000

    one_count = change // 1000
    change = change % 1000

    print("50,000원 지폐 : {}장".format(fifty_count))
    print("10,000원 지폐 : {}장".format(ten_count))
    print("5,000원 지폐 : {}장".format(five_count))
    print("1,000원 지폐 : {}장".format(one_count))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
