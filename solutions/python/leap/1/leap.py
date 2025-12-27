def leap_year(year):
    return ((year % 100) and not (year % 4))or (not (year % 100) and not (year % 400))
        
