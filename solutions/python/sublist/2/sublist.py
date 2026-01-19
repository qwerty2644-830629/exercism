# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    def is_include(big, small):
        for i in range(len(big) - len(small) +1):
            if small == big[i:i+len(small)]:
                return True
        return False
        
    if list_one == list_two:
        return EQUAL
    if is_include(list_one, list_two):
        return SUPERLIST
    if is_include(list_two, list_one):
        return SUBLIST
    return UNEQUAL
