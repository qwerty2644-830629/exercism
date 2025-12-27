import string

def rotate(text, key):
    cipher = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    ascii = str.maketrans(string.ascii_lowercase + string.ascii_uppercase, cipher + cipher.upper())

    return text.translate(ascii)