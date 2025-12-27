def to_rna(dna_strand):
    dna_dict = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    
    return ''.join([dna_dict[i] for i in dna_strand])