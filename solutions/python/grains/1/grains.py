def square(number):    
    if number == 1:
        return 1
    elif number <= 64 and number >=1:
        return square(number - 1) * 2
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total = 0
    for i in range(1,65):
        total += square(i)
    
    return total