# Game Constants
BOARD_LENGTH = 3
WINNING_LENGTH = 3

# Board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

# Tracking
turn_count = 0
x_turn = True


# Print Board
def printing_board() -> None:
    """
    Prints the rows in the board
    """
    for row in board:
        print(row)


# Input
def get_int(prompt: str) -> int:
    """
    Gets the required input from the user
    
    :param prompt: A string to tell the user what to input.
    :return: The `int` the user entered.
    """
    user_in = input(prompt)
    while not user_in.isnumeric():
        user_in = input(prompt)
    return int(user_in)


# Is it on the board?
def on_board(x: int, y: int) -> bool:
    """
    Checks if position x and y are located on the board

    :param x: The `int` for position x
    :param y: The `int` for position y
    :return: Whether or not x and y are available on the board
    """
    if x in range(BOARD_LENGTH) and y in range(BOARD_LENGTH):
        return True
    return False


# Player Position
def choosing(x: int, player_y: int) -> tuple[int, int] or None:
    """
    Uses the x and y input from the user, and places
    it on the board

    :param x: The `int` position of x on the board.
    :param player_y: The player side `int` on a cartesian
        plain. This is then converted to match the board.
    """
    global turn_count, x_turn
    y = WINNING_LENGTH - 1 - player_y

    if on_board(x, y):
        if board[y][x] == "-":
            if x_turn:
                board[y][x] = "X"
                x_turn = False
            else:
                board[y][x] = "O"
                x_turn = True
            turn_count += 1
            return x, y
        else:
            print("Position, x: {}, y: {}, is occupied by {}"
                  .format(x, player_y, board[y][x]))
    else:
        print("Position, x: {}, y: {}, is not in board".format(x, player_y))


# Win or Loss?
def checking(x: int, y: int, letter: int) -> str or None:
    """
    Checks if the previous move was a win or a loss for player `X`

    :param x: The `int` for position x
    :param y: The `int` for position y
    :param letter: The move played by
    :return: If `letter` has won, it returns a `str` stating that.
        If it was a draw, the `str` "Draw!" will be returned.
        Otherwise, nothing will be returned.
    """
    # Check Lists
    cl_row = [None] * (WINNING_LENGTH * 2 - 1) 
    cl_col = [None] * (WINNING_LENGTH * 2 - 1)  
    cl_pdia = [None] * (WINNING_LENGTH * 2 - 1) 
    cl_ndia = [None] * (WINNING_LENGTH * 2 - 1) 

    # Starting Positions for Extracting Positions
    starting_x = x - (WINNING_LENGTH - 1)
    starting_y = y + (WINNING_LENGTH - 1)

    # Negative Diagonal Starting Positions
    n_start_x = x + (WINNING_LENGTH - 1)
    n_start_y = y + (WINNING_LENGTH - 1)

    # Extracting Positions to the Check Lists
    for change in range(WINNING_LENGTH * 2 - 1):
        # Row
        if on_board(starting_x + change, y):
            cl_row[change] = board[y][starting_x + change]
        # Column
        if on_board(x, starting_y - change):
            cl_col[change] = board[starting_y - change][x]
        # Positive Diagonal
        if on_board(starting_x + change, starting_y - change):
            cl_pdia[change] = board[starting_y - change][starting_x + change]
        # Negative Diagonal
        if on_board(n_start_x - change, n_start_y - change):
            cl_ndia[change] = board[n_start_y - change][n_start_x - change]

    # Checking If There was any Winning Statements in the Check Lists
    if cl_row.count(letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if cl_col.count(letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if cl_pdia.count(letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if cl_ndia.count(letter) >= WINNING_LENGTH:
        return f"{letter} Won!"
    if turn_count == BOARD_LENGTH ** 2:
        return "Draw!"


# The Game
def main() -> None:
    """
    The game itself
    """
    global turn_count, x_turn

    play = True

    while play:

        while True:
            printing_board()
            
            coords = choosing(get_int(": "), get_int(": "))
            while coords is None:
                coords = choosing(get_int(": "), get_int(": "))
            outcome = checking(coords[0], coords[1], "X") 
            if outcome is not None:
                printing_board()
                print(outcome)
                break

            printing_board()

            coords = choosing(get_int(": "), get_int(": "))
            while coords is None:
                coords = choosing(get_int(": "), get_int(": "))
            outcome = checking(coords[0], coords[1], "O") 
            if outcome is not None:
                printing_board()
                print(outcome)
                break

        again = input("Would you like to play again (y/n): ")

        while again not in "y or n":
            again = input("Please enter `y` (`yes`) or `n` (`no`): ")
        if again.casefold() == "n":
            play = False
        else:
            turn_count = 0
            x_turn = True

            for row in board:
                for index, pos in enumerate(row):
                    row[index] = "-"


if __name__ == '__main__':
    main()
