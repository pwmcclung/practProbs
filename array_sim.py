def arrays_similar(seq1, seq2):
    if len(seq1) != len(seq2): 
        return False

    from collections import Counter
    count1 = Counter(seq1)
    count2 = Counter(seq2)

    return count1 == count2