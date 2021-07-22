def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        count = sum(1 for a, b in zip(strand_a, strand_b) if a != b)
        return count
    else:
        raise ValueError("Hamming distance can not be defined")
