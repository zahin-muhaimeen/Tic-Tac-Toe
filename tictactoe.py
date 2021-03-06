from tkinter import *
from tkinter import messagebox
from random import randint

# Initializing Tkinter
root = Tk()
root.title("Tic-Tac-Toe")

# Game Constants, Things to Keep Track Of
BOARD_LENGTH = 3
WINNING_LENGTH = 3
turn_count = 0
ai_previous = None


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
def checking(x: int, y: int, letter: str, winning_length: int = WINNING_LENGTH, ai_check: bool = False) -> str or None:
    """
    Checks if the previous move was a win or a loss for player `X`

    :param ai_check: Whether or not this function will be used
        for the AI
    :param winning_length: The `int` value representing how many
        `letter` in a row it needs to win
    :param x: The `int` for position x
    :param y: The `int` for position y
    :param letter: The move played by
    :return: If `letter` has won, it returns a `str` stating that.
        If it was a draw, the `str` "Draw!" will be returned.
        Otherwise, nothing will be returned.
    """
    # Check Lists
    cl_row = [None] * (winning_length * 2 - 1)
    cl_col = [None] * (winning_length * 2 - 1)
    cl_pdia = [None] * (winning_length * 2 - 1)
    cl_ndia = [None] * (winning_length * 2 - 1)

    # Starting Positions for Extracting Positions
    starting_x = x - (winning_length - 1)
    starting_y = y + (winning_length - 1)

    # Negative Diagonal Starting Positions
    n_start_x = x + (winning_length - 1)
    n_start_y = y + (winning_length - 1)

    # Extracting Positions to the Check Lists
    for change in range(winning_length * 2 - 1):
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
    if cl_row.count(letter) >= winning_length:
        if ai_check:
            return "row"
        return f"{letter} Won!"
    if cl_col.count(letter) >= winning_length:
        if ai_check:
            return "col"
        return f"{letter} Won!"
    if cl_pdia.count(letter) >= winning_length:
        if ai_check:
            return "pdia"
        return f"{letter} Won!"
    if cl_ndia.count(letter) >= winning_length:
        if ai_check:
            return "ndia"
        return f"{letter} Won!"
    if turn_count == BOARD_LENGTH ** 2:
        return "Draw!"


# Reset
def game_reset():
    """
    Resets the entire game
    """
    global turn_count, ai_previous

    turn_count = 0
    ai_previous = None
    for row in board:
        for col in row:
            col["text"] = " "


# Artificial Offense
def ai_offense(x: int, y: int) -> tuple[int, int] or None:
    """Finds the move that causes the ai to win"""
    ai_outcome = checking(x, y, "O", winning_length=WINNING_LENGTH - 1, ai_check=True)

    if ai_outcome is not None:
        if ai_outcome == "row":
            for this_x, col in enumerate(board[y]):
                if col["text"] == " ":
                    return this_x, y

        if ai_outcome == "col":
            for this_y, row in enumerate(board):
                if row[x]["text"] == " ":
                    return x, this_y

        if ai_outcome == "ndia":
            for index in range(BOARD_LENGTH):
                if board[index][index]["text"] == " ":
                    return index, index

        if ai_outcome == "pdia":
            for index in range(BOARD_LENGTH):
                if board[BOARD_LENGTH - 1 - index][index]["text"] == " ":
                    return index, BOARD_LENGTH - 1 - index


# Artificial Defense
def ai_defense(x: int, y: int) -> tuple[int, int] or None:
    """Finds the move that prevents the player from winning"""
    ai_outcome = checking(x, y, "X", winning_length=WINNING_LENGTH - 1, ai_check=True)

    if ai_outcome is not None:
        if ai_outcome == "row":
            for this_x, col in enumerate(board[y]):
                if col["text"] == " ":
                    return this_x, y

        if ai_outcome == "col":
            for this_y, row in enumerate(board):
                if row[x]["text"] == " ":
                    return x, this_y

        if ai_outcome == "ndia":
            for index in range(BOARD_LENGTH):
                if board[index][index]["text"] == " ":
                    return index, index

        if ai_outcome == "pdia":
            for index in range(BOARD_LENGTH):
                if board[BOARD_LENGTH - 1 - index][index]["text"] == " ":
                    return index, BOARD_LENGTH - 1 - index


# Artificial Intelligence
def ai(x: int, y: int, pre_move: int) -> tuple[int, int]:
    """
    Finds the best possible position to play

    :param x: Player move x
    :param y: Player move y
    :param pre_move: Previous AI move
    :return: The best possible position in x and y coordinates
    """

    if turn_count == 1:
        places = ((0, 2), (2, 2), (2, 0), (0, 0))
        position = randint(0, 3)
        while board[places[position][1]][places[position][0]]["text"] == "X":
            position = randint(0, 3)
        else:
            return places[position]

    move_offense = ai_offense(pre_move[0], pre_move[1])
    if move_offense is not None:
        return move_offense

    move_defense = ai_defense(x, y)
    if move_defense is not None:
        return move_defense

    for this_y, row in enumerate(board):
        for this_x, col in enumerate(row):
            if col["text"] == " ":
                return this_x, this_y


# Button Functionality
def b_click(button: Button) -> None:
    """
    Allows Tic Tac Toe button functionality when it is pressed

    :param button: The button pressed
    """
    global turn_count, ai_previous

    coordinates = button.grid_info()
    x = int(coordinates["column"])
    y = int(coordinates["row"])

    if button["text"] == " ":
        button["text"] = "X"
        turn_count += 1
        outcome = checking(x, y, "X")
        if outcome is not None:
            messagebox.showinfo("Tic Tac Toe", outcome)
            game_reset()
        else:
            ai_coord = ai(x, y, ai_previous)
            ai_previous = ai_coord
            turn_count += 1
            board[ai_coord[1]][ai_coord[0]]["text"] = "O"
            outcome = checking(ai_coord[0], ai_coord[1], "O")
            if outcome is not None:
                messagebox.showinfo("Tic Tac Toe", outcome)
                game_reset()
    else:
        messagebox.showerror("Tic Tac Toe", f"Position Occupied by Player {button['text']}")


# Buttons
b1 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b7))                                           
b8 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
            command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 25), height=4, width=8, bg="#232731", fg="#ABB2BF",
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
