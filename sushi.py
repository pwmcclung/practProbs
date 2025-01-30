def total_bill(s):
    lst_s = list(s)
    cost = 0
    count = 0
    while len(lst_s) > 0:
        item = lst_s.pop(0)
        count += 1
        if item == ' ':
            count -= 1
        else:
            if count % 5 == 0:
                pass
            else:
                cost += 2
    return cost