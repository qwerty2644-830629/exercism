def rotate(text, key): 
    ascii = [int(ord(i)) for i in text]
    
    for i in range(len(ascii)):
        if 65 <= ascii[i] <= 90 or 97 <= ascii[i] <= 122:
            if 90 >= ascii[i] >= 65 and ascii[i] + key > 90: ascii[i] = chr(ascii[i] + key - 26) 
            elif ascii[i] >= 97 and ascii[i] + key > 122: ascii[i] = chr(ascii[i] + key - 26)
            else: ascii[i] = chr(ascii[i] + key)
        else:
            ascii[i] = chr(ascii[i])
    return ''.join(ascii)