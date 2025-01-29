def valid_ISBN10(isbn): 
    if len(isbn) != 10:
        return False

    total = 0
    for i, char in enumerate(isbn):
        if i < 9:
            if not char.isdigit():
                return False
            total += int(char) * (i + 1)
        else:
            if char == 'X':
                total += 10 * (i + 1)
            elif char.isdigit():
                total += int(char) * (i + 1)
            else:
                return False

    return total % 11 == 0