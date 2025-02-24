def sort_by_exclusion(words):

    n = len(words)
    
    #1. Handle the base case of an empty list (shouldn't happen according to the problem statement, but good practice).
    if n == 0:
        return 0

    #2. Initialize DP table. dp[i] stores the minimum number of removals needed to make the sublist words[:i+1] strictly ascending.
    dp = [1] * n  # Initialize with 1 because at least one element can always be kept.


    #3. Iterate through the list, building up the DP table.
    for i in range(1, n):
        dp[i] = 1  # Initialize with 1 (keeping only the current element).
        for j in range(i):
            if words[i] > words[j]: # Check for strictly ascending order.
                dp[i] = max(dp[i], dp[j] + 1) #Update dp[i] if including the current word improves the strictly ascending subsequence length.

    #4. Find the maximum length of a strictly ascending subsequence (this is the number of words *kept*).
    max_len = max(dp)
    
    #5. The number of words to remove is the difference between the original list length and the maximum strictly ascending subsequence length.
    return n - max_len