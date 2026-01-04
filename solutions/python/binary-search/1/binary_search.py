def find(search_list, value):
    min_number = 0
    max_number = len(search_list) -1

    while True:
        if max_number < min_number: 
            raise ValueError("value not in array")
            break
            
        middle = max_number + min_number
        if value == search_list[middle]: return middle
        elif value > search_list[middle]: min_number = middle + 1 
        else: max_number = middle - 1
