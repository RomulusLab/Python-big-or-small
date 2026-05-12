def to_rna(dna_strand):
    result = ''
    
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    
    for letter in dna_strand:
        if letter in dna_to_rna:
            result += dna_to_rna[letter]

    return result
    