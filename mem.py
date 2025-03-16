def unscramble(scramble):
    global word_list

    # Create a memoized data structure for fast hashing
    anagram_dict = {}
    for word in word_list:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    # Sort the scrambled word to find anagrams
    sorted_scramble = "".join(sorted(scramble))

    # Return the list of anagrams if found, otherwise return an empty list
    if sorted_scramble in anagram_dict:
        return anagram_dict[sorted_scramble]
    else:
        return []