def rotate(text, key): 
    ascii = [int(ord(i)) for i in text]
    
    for i in ascii:
        if 65 <= i <= 90 or 97 <= i <= 122:
            if 90 >= i >= 65 and i + key > 90: ascii[ascii.index(i)] = chr(i + key - 26) 
            elif i >= 97 and i + key > 122: ascii[ascii.index(i)] = chr(i + key - 26)
            else: ascii[ascii.index(i)] = chr(i + key)
        else:
            ascii[ascii.index(i)] = chr(i)
    return ''.join(ascii)