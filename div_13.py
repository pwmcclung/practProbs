def thirt(n):
    remainders = [1, 10, 9, 12, 3, 4]
    n_str = str(n)
    
    while True:
        new_n = 0
        for i, digit in enumerate(reversed(n_str)): 
            new_n += int(digit) * remainders[i % 6]
        if new_n < 100:
            return new_n
        n_str = str(new_n)