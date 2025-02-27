def find_constant(arr, lb, ub):
    min_val = min(arr)
    max_val = max(arr)
    
    constant = (min_val - lb + max_val - ub) / 2.0
    
    return constant