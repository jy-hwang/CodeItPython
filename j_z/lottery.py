# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 코드를 입력하세요
    numbers = [1, 2, 3, 4, 5, 6]
    return numbers


# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    # 코드를 입력하세요
    winning_numbers = [1, 2, 3, 4, 5, 6, 7]
    return winning_numbers


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # 코드를 입력하세요
    i = 0
    while i < len(list1) - 1:
        count = list1[i] in list2
        i = i + 1
    return count


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 코드를 입력하세요
    x = count_matching_numbers(numbers, winning_numbers)
    print(x)

    if x == 6:
        return 1000000000
    elif x == 5:
        return 1000000
    elif x == 4:
        return 50000
    else:
        return 5000
