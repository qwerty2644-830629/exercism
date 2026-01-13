def sum_of_multiples(limit, multiples):
    solution = sum({i for n in multiples if n != 0 for i in range(n, limit, n)})
    
    return solution
    