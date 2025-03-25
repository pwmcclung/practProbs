def estimator(obstacles, stamina):
    num_list = map(str, obstacles)
    num_list_nums = ''.join(num_list).split('0')
    score = 0
    for x in num_list_nums:
        if x == '1':
            score += 2
        if x == '11':
            score += 5
        if x == '111':
            score += 10
    if score > stamina:
        return False
    else:
        return True