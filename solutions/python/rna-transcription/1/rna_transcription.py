def to_rna(dna_strand):
    dna_list = []
    
    for i in dna_strand:
        if i == 'G': dna_list.append('C')
        elif i == 'C': dna_list.append('G')
        elif i == 'A': dna_list.append('U')
        elif i == 'T': dna_list.append('A')
        else:  dna_list.append('')

    return ''.join(dna_list)
