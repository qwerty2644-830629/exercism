# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
        
    if len(list_one) > len(list_two):
        for i in range(len(list_one) - len(list_two) +1):
            if list_two == list_one[i:i+len(list_two)]:
                return SUPERLIST
        return UNEQUAL
        
    else:
        for i in range(len(list_two) - len(list_one) +1):
            if list_one == list_two[i:i+len(list_one)]:
                return SUBLIST
        return UNEQUAL
