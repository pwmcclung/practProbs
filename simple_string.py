def string_expansion(s):
    if not s:
        return ""

    expanded_string = ""
    current_repeat = 1
    i = 0
    while i < len(s):
        if s[i].isdigit():
            
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            
            current_repeat = int(s[j-1])
            i = j
        
        elif s[i].isalpha():
            expanded_string += s[i] * current_repeat
            i += 1
        else:
            i += 1 

    return expanded_string