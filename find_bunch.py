def find_arr(arrA, arrB, rng, wanted):

    lower_bound, upper_bound = rng

    countA = {}
    for num in arrA:
        countA[num] = countA.get(num, 0) + 1

    countB = {}
    for num in arrB:
        countB[num] = countB.get(num, 0) + 1

    result = []
    for num in set(arrA) & set(arrB): 
        if countA.get(num, 0) > 1 and countB.get(num, 0) > 1 and lower_bound <= num <= upper_bound:
            if wanted == 'odd' and num % 2 != 0:
                result.append(num)
            elif wanted == 'even' and num % 2 == 0:
                result.append(num)

    result.sort()
    return result