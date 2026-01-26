def factors(value):
    given_number = []
    num = 2
    
    while value != 1:
        if value % num == 0:
            given_number.append(num)
            value /= num
        else:
            num += 1
     
    return given_number
    