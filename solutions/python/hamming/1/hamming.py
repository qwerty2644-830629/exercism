def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    distance = 0
    for i, dna_a in enumerate(strand_a):
        if dna_a != strand_b[i]: distance += 1
            
    return distance
    