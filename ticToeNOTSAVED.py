def is_solved(board):
     # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # Check for empty spots
    for row in board:
        if 0 in row:
            return -1

    # It's a draw
    return 0