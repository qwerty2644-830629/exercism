def append(list1, list2):
    for i in list2: list1.append(i)
    return list1

    
def concat(lists):
    list1 = []
    for i in lists: append(list1, i)
    return list1
    

def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    return len(list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    for i in list: initial = function(initial, i)
    return initial


def foldr(function, list, initial):
    for i in reverse(list): initial = function(initial, i)
    return initial


def reverse(list):
    return [list[len(list) - 1 - i] for i in range(len(list))]
