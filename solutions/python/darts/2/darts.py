def score(x, y):
    distance = x ** 2 + y ** 2

    if distance > 10 ** 2: point = 0
    elif distance > 5 ** 2: point = 1
    elif distance > 1 ** 2: point = 5
    else: point = 10

    return point