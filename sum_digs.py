def sum_dig_nth_term(init_val, pattern_l, nth_term):
    term = init_val
    for i in range(1, nth_term):
        term += pattern_l[(i - 1) % len(pattern_l)]

    sum_digits = 0
    for digit in str(term):
        sum_digits += int(digit)

    return sum_digits