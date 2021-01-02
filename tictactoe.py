from random import randint

# Game Constans
BOARD_LENGTH = 3
WINNING_LENGTH = 3

# Board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

# Tracking
turns = 0
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


# Player Position
def choosing(x: int, player_y: int) -> None:
    """
    Uses the x and y input from the user, and places
    it on the board

    :param x: The `int` position of x on the board.
    :param player_y: The player side `int` on a cartesian
        plain. This is then converted to match the board.
    """
    global turns, x_turn
    y = WINNING_LENGTH - 1 - player_y

    if x in range(BOARD_LENGTH) and y in range(BOARD_LENGTH):
        if board[y][x] == "-":
            if x_turn:
                board[y][x] = "X"
                x_turn = False
                turns += 1
            else:
                board[y][x] = "O"
                x_turn = True
                turns += 1
        else:
            print("Position, x: {}, y: {}, is occupied by {}"
                  .format(x, player_y, board[y][x]))
    else:
        print("Position, x: {}, y: {}, is not in board".format(x, player_y))


# Checks if Won
def checking(moved: str) -> str or None:
    """
    Checks if the present move caused a winning move
    or caused a draw.

    :param moved: Whoever chose the present move
    :return: If the move caused a win, it returns
        a `str` telling the player who won. If its a
        draw it will return the `str` "Draw!".
        Otherwise, nothing will be returned.
    """
    if turns >= 5:

        # Check List
        check_list = [None] * BOARD_LENGTH

        # Row
        for row in board:
            if row.count(moved) == WINNING_LENGTH:
                return "{} Won!".format(moved)

        # Column
        for index in range(BOARD_LENGTH):
            for pos, row in enumerate(board):
                check_list[pos] = row[index]

            if check_list.count(moved) == WINNING_LENGTH:
                return "{} Won!".format(moved)

        # Negative Diagonal
        for index in range(BOARD_LENGTH):
            for row in board:
                check_list[index] = board[index][index]

        if check_list.count(moved) == WINNING_LENGTH:
            return "{} Won!".format(moved)

        # Positive Diagonal
        for index in range(BOARD_LENGTH):
            for row in board:
                check_list[index] = board[BOARD_LENGTH - 1 - index][index]

        if check_list.count(moved) == WINNING_LENGTH:
            return "{} Won!".format(moved)

        # Draw
        if turns == BOARD_LENGTH ** 2:
            return "Draw!"


# The Game
def main() -> None:
    """
    The game itself
    """
    global turns, x_turn

    play = True

    while play:

        while True:
            printing_board()

            choosing(get_int(": "), get_int(": "))
            if checking("X") is not None:
                printing_board()
                print(checking("X"))
                break

            printing_board()

            choosing(get_int(": "), get_int(": "))
            if checking("O") is not None:
                printing_board()
                print(checking("O"))
                break

        again = input("Would you like to play again (y/n): ")

        while again not in "y or n":
            again = input("Please enter `y` (`yes`) or `n` (`no`): ")
        if again.casefold() == "n":
            play = False
        else:
            turns = 0
            x_turn = True

            for row in board:
                for index, pos in enumerate(row):
                    row[index] = "-"


if __name__ == '__main__':
    main()
