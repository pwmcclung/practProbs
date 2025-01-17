def zero_plentiful(arr):

    # Initialize the count of zero sequences
    zero_sequence_count = 0
    # Initialize the length of the current zero sequence
    current_zero_length = 0
    # Flag to track if we've encountered at least one zero sequence
    found_zeros = False

    # Iterate over the elements of the array
    for num in arr:
        # If the current number is 0, increment the current_zero_length
        if num == 0:
            current_zero_length += 1
            found_zeros = True  # mark that at least one zero has been found
        else:
            # If the current number is not 0, check if we were in a zero sequence
            if current_zero_length > 0:
                # If the length of the previous zero sequence is less than 4, it's not zero-plentiful
                if current_zero_length < 4:
                    return 0
                # If the length of the previous zero sequence is 4 or more, increment zero_sequence_count
                else:
                    zero_sequence_count += 1
                # Reset current_zero_length for a new sequence
                current_zero_length = 0

    # After the loop finishes, check if there was a trailing zero sequence
    if current_zero_length > 0:
        if current_zero_length < 4: # trailing sequence less than 4 - not zero plentiful
            return 0
        else:  #trailing sequence is valid
            zero_sequence_count += 1  
    # If we did not find any zeros
    if not found_zeros:
        return 0

    # Return the final count of zero sequences if all of them met the criteria (or zero if not)
    return zero_sequence_count