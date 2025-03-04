def circularly_sorted(arr):
    if not arr:
        return True

    n = len(arr)
    num_decreases = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            num_decreases += 1

    return num_decreases <= 1