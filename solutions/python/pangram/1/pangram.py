import string

def is_pangram(text):

    alphabet = set(string.ascii_lowercase) # all lower letter 
    text_set = set(text.lower())
    
    return alphabet <= text_set # text_set is in alphabet ? 