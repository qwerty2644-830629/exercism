def is_armstrong_number(number):
    number_new = list(str(number))
    y = len(number_new)
    total = 0
    
    for x in number_new:
        total += int(x) ** y
        
    return total == number