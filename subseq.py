def count_subsequences(needle, haystack):
    needle_len = len(needle)
    haystack_len = len(haystack)
    
    
    dp = {}

    def count_recursive(needle_index, haystack_index):
        if needle_index == needle_len:
            return 1
        if haystack_index == haystack_len:
            return 0
        
        if (needle_index, haystack_index) in dp:
            return dp[(needle_index, haystack_index)]

        count = 0
        if needle[needle_index] == haystack[haystack_index]:
            count += count_recursive(needle_index + 1, haystack_index + 1)
        count += count_recursive(needle_index, haystack_index + 1)

        dp[(needle_index, haystack_index)] = count
        return count

    result = count_recursive(0, 0)
    return result % (10**8)