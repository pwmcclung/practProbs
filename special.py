import collections
def calculate_ssw(word):
    score = 0
    letter_counts = collections.Counter(word)
    for letter, frequency in letter_counts.items():
        score += ord(letter) * frequency
    return score
def find_word(num_let, max_ssw):
    global WORD_LIST 
    best_word_found = None
    highest_ssw_found = -1 
    for word in WORD_LIST: 
        if len(word) == num_let:
            current_ssw = calculate_ssw(word)
            if current_ssw <= max_ssw:
                if current_ssw > highest_ssw_found:
                    highest_ssw_found = current_ssw
                    best_word_found = word
                elif current_ssw == highest_ssw_found:
                    if best_word_found is None or word > best_word_found:
                        best_word_found = word              
    return best_word_found