def square_root(number):
    max = 400
    min = 0
   
    while max > min:
        mid = int((min + max)/ 2)
        print(max, min, mid)
        if number == mid ** 2:
            return mid
        elif number > mid ** 2:
            min = mid
        else:
            max = mid
            
    raise ValueError("not a square root")
    