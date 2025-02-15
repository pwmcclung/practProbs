def check_password(s):
    letters_lower = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't', 'u', 'v', 'w', 'x', 'y','z']
    letters_capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3','4','5','6','7','8', '9']
    chars = ['!', '@','#','$','%','^','&','*','?']
    if len(s) < 8 or len(s) > 20:
        return 'not valid'
    s_list = list(s)
    lower_count = 0
    upper_count = 0
    digits_count = 0
    chars_count = 0
    not_allowed = 0
    for x in s_list:
        if x in letters_lower:
            lower_count += 1
        elif  x in letters_capitals:
            upper_count += 1
        elif x in digits:
            digits_count += 1
        elif x in chars:
            chars_count += 1
        else: 
            not_allowed += 1
    if not_allowed > 0:
        return 'not valid'
    else:
        if lower_count > 0 and upper_count > 0 and digits_count > 0 and chars_count > 0:
            return 'valid'
        else:
            return 'not valid'