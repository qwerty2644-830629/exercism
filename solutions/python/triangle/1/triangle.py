def equilateral(sides): # a = b = c 
    return max(sides) == min(sides) and not min(sides) == 0


def isosceles(sides):
    a, b, c =equal(sides)
    return (a == b or b == c) and a <= b + c and not min(sides) == 0



def scalene(sides):
    a, b, c = equal(sides)
    return a <= b + c and not isosceles(sides)


def equal(sides):
    a, b, c = sides
    if b < c: b, c = c, b
    if a < b: a, b = b, a
    if b < c: b, c = c, b

    return [a, b, c]