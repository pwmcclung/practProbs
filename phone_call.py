def phone_call(min1, min2_10, min11, s):
    min_10_cost = (min1 * 1) + (min2_10 * 9)
    min_1_cost = min1 * 1
    if s > min_10_cost:
        return 10 + (s-min_10_cost) // min11
    elif s < min_10_cost and s  > min1:
        return 1 + (s - min1) // min2_10
    elif s == min1:
        return 1
    else:
        return 0