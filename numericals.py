from collections import defaultdict

def numericals(s):

    counts = defaultdict(int)  
    result = ""
    for char in s:
        counts[char] += 1
        result += str(counts[char])  
    return result