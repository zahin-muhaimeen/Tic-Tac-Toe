from random import randint

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

turns = 0
x_turn = True


def printing_board():
    for row in board:
        print(row)


def get_int(prompt):
    user_in = input(prompt)
    while not user_in.isnumeric():
        user_in = input(prompt)
    return int(user_in)


def choosing(x, player_y):
    global turns, x_turn
    y = 2 - player_y

    if x in range(3) and y in range(3):
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
            print("Position, x: {}, y: {}, is occupied by {}".format(x, player_y, board[y][x]))
    else:
        print("Position, x: {}, y: {}, is not in board".format(x, player_y))


def checking(moved):
    if turns >= 5:
        # Check List
        check_list = [None, None, None]
        # Row
        for row in board:
            if row.count(moved) == 3:
                return "{} Won!".format(moved)
        # Column
        for index in range(len(board)):
            for pos, row in enumerate(board):
                check_list[pos] = row[index]
            if check_list.count(moved) == 3:
                return "{} Won!".format(moved)
        # Negative Diagonal
        for index in range(len(board)):
            for row in board:
                check_list[index] = board[index][index]
        if check_list.count(moved) == 3:
            return "{} Won!".format(moved)
        # Positive Diagonal
        for index in range(len(board)):
            for row in board:
                check_list[index] = board[2 - index][index]
        if check_list.count(moved) == 3:
            return "{} Won!".format(moved)
        # Draw
        if turns == 9:
            return "Draw!"


def main():
    global turns, x_turn

    play = True
    while play:
        while True:
            printing_board()
            choosing(get_int(": "), get_int(": "))
            if checking("X") != None:
                printing_board()
                print(checking("X"))
                break
            printing_board()
            choosing(get_int(": "), get_int(": "))
            if checking("O") != None:
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
                for index, pos in row:
                    row[index] = "-"


if __name__ == '__main__':
    main()
