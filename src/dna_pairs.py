def dna_pairs(dna_string):
    dna_pairs = []
    for dna in dna_string:
        if dna == "G":
            dna_pairs.append(["G", "C"])
        elif dna == "C":
            dna_pairs.append(["C", "G"])
        elif dna == "A":
            dna_pairs.append(["A", "T"])
        elif dna == "T":
            dna_pairs.append(["T", "A"])
        
    return dna_pairs
