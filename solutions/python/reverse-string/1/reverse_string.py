def reverse(text):
    a = list(text)
    b = ''
    for i in range(len(a)-1, -1, -1): b += a[i]
    
    return b