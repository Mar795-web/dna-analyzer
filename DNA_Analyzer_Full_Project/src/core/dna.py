from collections import Counter

def validate_sequence(seq:str)->str:
    seq = seq.strip().upper()
    if not seq:
        raise ValueError("Empty sequence.")
    if any(c not in "ATGC" for c in seq):
        raise ValueError("Only A,T,G,C are allowed.")
    return seq

def length(seq):
    return len(validate_sequence(seq))

def calculate_gc(seq):
    seq=validate_sequence(seq)
    return round((seq.count("G")+seq.count("C"))/len(seq)*100,2)

def nucleotide_count(seq):
    seq=validate_sequence(seq)
    return dict(Counter(seq))

def reverse_complement(seq):
    seq=validate_sequence(seq)
    return seq.translate(str.maketrans("ATGC","TACG"))[::-1]

def transcribe_rna(seq):
    return validate_sequence(seq).replace("T","U")
