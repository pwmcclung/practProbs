def reverse_odd_count(array):
    counts = {}
    for el in array:
        counts[el] = counts.get(el, 0) + 1
    odd_els = [el for el in array if counts[el] % 2 != 0]
    
    rev_odd = odd_els[::-1]
    
    res = []
    odd_idx = 0
    for el in array:
        if counts[el] % 2 != 0:
            res.append(rev_odd[odd_idx])
            odd_idx += 1
        else:
            res.append(el)
    return res