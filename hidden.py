def hidden(num):
    lst_num = list(str(num))
    key_dict = {'6':'a', '1':'b', '7':'d', '4':'e', '3':'i', '2':'l', '9':'m', '8':'n','0':'o','5':'t'}
    new_str = ''
    for x in lst_num:
        new_str += key_dict[x]
    return new_str