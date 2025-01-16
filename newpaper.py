def cheapest_quote(n):
    tc = 0
    sales = n
    while sales != 0:
        if sales > 39:
            while sales > 39:
                tc += 3.85
                sales -= 40
        if sales > 19:
            while sales > 19:
                tc += 1.93
                sales -= 20
        if sales > 9:
            while sales > 9:
                tc += 0.97
                sales -= 10
        if sales > 4:
            while sales > 4:
                tc += 0.49
                sales -= 5
        if sales > 0:
            while sales > 0:
                tc += 0.10
                sales -= 1
    return round(tc,2)
    