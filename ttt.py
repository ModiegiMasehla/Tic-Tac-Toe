def find_line_winner(board):
    '''
    Check every row, column and diagonal of a 3x3 board for a winner.

    This does no validation, so it also works on boards with empty
    cells (""). Use find_winner for validated, full boards.

    :param board: 3x3 list of lists containing "X", "O" or "".
    :return: "X" or "O" if a player has three in a line, otherwise None.
    '''
    for i in board:                                    #for the items in the board row
        if i[0]== i[1]== i[2] and i[0] != "":             #if all 3 items in range 0 to 2 are the same and not an empty string
            return i[0]                                    #return the winner


    for col in range(3):                                                           # for the columns restrict the range to 3
        if board[0][col]== board[1][col]==board[2][col] and board [0][col] != "":   #if the item in the columns at the index 0,1 and 2 are all equal and nopt empty
            return board[0][col]                                                        #return the winner

    if board[0][0]== board[1][1]==board[2][2] and board [0][0] != "":            #if the items on the board placed diagonally are the same
        return board[0][0]                                                        #given that the item is not empty return the winner which is


    if board [2][0]==board[1][1]==board[0][2] and board [0][2] != "":         #check the opposite diagonal
        return board[0][2]

    return None


def find_winner(board):
    '''
    Find the winner of a finished Tic-Tac-Toe game.

    :param board: 3x3 list of lists. Every cell must be "X" or "O".
    :return: "X" or "O" if that player has three in a row, column or
        diagonal, otherwise None.
    :raises ValueError: if the board does not have exactly 3 rows of 3
        cells, or if any cell is not "X" or "O" (empty cells are rejected).
    '''
    ttt=("X", "O")                   # a variable assigned to the valid board options


    if len(board) !=3:                 #ensure that the board has 3 rows and 3 columns, if not raise Value Error
        raise ValueError()              #ensure that the shape of the board is correct

    for col in board:                     #for items in the columns of the board they must be equal to 3 for a valid shape
        if len(col)!=3:
            raise ValueError()


    for col in board:                          #for the columns in the board
        for i in col:                           #for items in the columns in the board
            if i not in ttt and i != "":         #if the item is not "X" or "O" it is an invalid item and must return value error
                raise ValueError()


    for col in board:
        for i in col:
            if i == "":                       #if the item in the column of the board are empty return value error
                raise ValueError()

    return find_line_winner(board)
