def get_the_vowels(word):
    count = 0
    list_word = list(word)
    vowels = list('aeiou')
    list_word_comp = [x for x in list_word if x in vowels]
    while len(list_word_comp) > 0:
        first = list_word_comp.pop(0)
        if first == vowels[0]:
            count += 1
            a = vowels.pop(0)
            vowels.append(a)
    return count
        