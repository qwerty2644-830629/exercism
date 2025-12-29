def is_valid(isbn):
    isbn = isbn.replace('-', '')
    total = 0
    if not len(isbn) == 10: return False
    
    for i in range(10):
        if ord(isbn[i]) == ord('X') and i == 9: total += 10 * (10 - i)
        elif 65 <= ord(isbn[i]) <= 90: return False 
        else: total += int(isbn[i]) * (10 - i)
        print(total)

    return total % 11 == 0