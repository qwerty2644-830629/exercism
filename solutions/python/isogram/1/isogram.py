def is_isogram(string):
    string = string.replace(' ', '')
    string = string.replace('-', '')
    dictionary = {}
    for i in string.lower():
        dictionary[i] = dictionary.get(i,0) + 1
    print(dictionary)

    for letter, time in dictionary.items():
        if time > 1:
            return False

    return True