def rotate(text, key):
    new_text = ''    
    ascii = [int(ord(i)) for i in text]

    for i in ascii:
        if 65 <= i <= 90 or 97 <= i <= 122:
            print(i, i + key, chr(i+key))
            if 90 >= i >= 65 and i + key > 90: new_text += chr(i + key - 26)
            elif i >= 97 and i + key > 122: new_text += chr(i + key - 26)
            else: new_text += chr(i + key)
        else:
            new_text += chr(i)
    
    return new_text        