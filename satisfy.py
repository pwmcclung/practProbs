import math
def smallest(n):

    lcm = 1
    
    for i in range(1, n + 1):
        gcd_val = math.gcd(i, lcm)
        lcm = (lcm * i) // gcd_val
        
    return lcm