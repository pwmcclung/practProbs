def convert(st):
    new_st = ''
    st_list = list(st)
    for x in range(len(st_list)):
        if st_list[x] == 'a':
            new_st += 'o'
        elif st_list[x] == 'o':
            new_st += 'u'
        else:
            new_st += st_list[x]
    return new_st