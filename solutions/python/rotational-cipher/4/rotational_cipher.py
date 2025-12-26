import string

def rotate(text, key):
    a = list(string.ascii_lowercase)+list(string.ascii_uppercase)
    b = [ord(i)+key for i in string.ascii_lowercase]
    c = [ord(i)+key for i in string.ascii_uppercase]
    for i in b: 
        if i > 122: b[b.index(i)] -= 26
    for i in c: 
        if i > 90: c[c.index(i)] -= 26
    print(str([chr(i) for i in b]+[chr(i) for i in c]))
    ascii = str.maketrans(str(a), str([chr(i) for i in b]+[chr(i) for i in c]))
    
    return  text.translate(ascii)