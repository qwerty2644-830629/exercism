import string

def rotate(text, key):
    a = list(string.ascii_lowercase)+list(string.ascii_uppercase)
    b = []
    for i in string.ascii_lowercase: 
        if ord(i) + key > 122: b.append(ord(i) + key - 26)
        else: b.append(ord(i) + key)
    for i in  string.ascii_uppercase: 
        if ord(i) + key > 90: b.append(ord(i) + key - 26)
        else: b.append(ord(i) + key)
    print(b, str([chr(i) for i in b]))
    ascii = str.maketrans(str(a), str([chr(i) for i in b]))
    
    return  text.translate(ascii)