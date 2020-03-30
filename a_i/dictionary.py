lists = [3, 4, 1, 2, 7]

print(lists[1])

# 사전
# dictionary :  key - value

dict1 = {}
print(type(dict1))

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)

family = {}

family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'

print(family)
print(family.keys())
print(family.values())

print('son' in family.keys())
print('uncle' in family.keys())

family_keys = list(family.values())

print(family_keys)
print(type(family_keys))
