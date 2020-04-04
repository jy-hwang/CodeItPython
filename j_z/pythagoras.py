for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if c ** 2 == a ** 2 + b ** 2 and c > b > a:
            # if c > b > a: #and (c * c == a * a + b * b):
            print(c, b, a, a * b * c)
