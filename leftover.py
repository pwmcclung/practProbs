def round_to_five(arr):
    new_arr = []
    for x in arr:
        leftover = x % 5
        if leftover < 2.49:
            new_arr.append(x-leftover)
        elif leftover > 2.49:
            new_arr.append((x-leftover) + 5)
        else:
            new_arr.append(x)
    return new_arr