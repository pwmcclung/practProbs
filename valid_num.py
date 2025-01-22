def validate_base(num, base):
    list_num = list(num)
    pos_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_max = max(list_num)
    idx = pos_str.index(l_max)
    if idx < base:
        return True
    else:
        return False