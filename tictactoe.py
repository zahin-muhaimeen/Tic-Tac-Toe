from tkinter import *
from tkinter import messagebox

# Intializing Tkinter
root = Tk()
root.title("Tic-Tac-Toe")

# Game Constants, Things to Keep Track Of
BOARD_LENGTH = 3
WINNING_LENGTH = 3
turn_count = 0
x_turn = True


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


# Win or Loss?
def checking(x: int, y: int, letter: str) -> str or None:
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
            cl_row[change] = board[y][starting_x + change]["text"]
        # Column
        if on_board(x, starting_y - change):
            cl_col[change] = board[starting_y - change][x]["text"]
        # Positive Diagonal
        if on_board(starting_x + change, starting_y - change):
            cl_pdia[change] = board[starting_y - change][starting_x + change]["text"]
        # Negative Diagonal
        if on_board(n_start_x - change, n_start_y - change):
            cl_ndia[change] = board[n_start_y - change][n_start_x - change]["text"]

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


# Reset
def game_reset():
    """
    Resets the entire game
    """
    global x_turn, turn_count

    x_turn = True
    turn_count = 0
    for row in board:
        for col in row:
            col["text"] = " "


# Button Functionality
def b_click(button: Button) -> None:
    """
    Allows Tic Tac Toe button functionaly when it is pressed

    :param button: The button pressed
    """
    global x_turn, turn_count

    coordinates = button.grid_info()
    x = int(coordinates["column"])
    y = int(coordinates["row"])

    if button["text"] == " ":
        if x_turn:
            button["text"] = "X"
            x_turn = False
            turn_count += 1
            outcome = checking(x, y, "X")
            if outcome is not None:
                messagebox.showinfo("Tic Tac Toe", outcome)
                game_reset()
        else:
            button["text"] = "O"
            x_turn = True
            turn_count += 1
            outcome = checking(x, y, "O")
            if outcome is not None:
                messagebox.showinfo("Tic Tac Toe", outcome)
                game_reset()
    else:
        messagebox.showerror("Tic Tac Toe", "Position Ouccupied by Player {}"
                             .format(button["text"]))


# Buttons
b1 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="SystemButtonFace",
            command=lambda: b_click(b9))

# Board
board = [[b1, b2, b3],
         [b4, b5, b6],
         [b7, b8, b9],
         ]

for y, row in enumerate(board):
    for x, col in enumerate(row):
        col.grid(row=y, column=x)

root.mainloop()
