def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        i = i + 1
    return False


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))

print(7 in primes)
print(12 in primes)
print(23 not in primes)

# 리스트 안의 리스트 (Nested List)
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

print(grades[0])
print(grades[0][1])
print(grades[0][0])
