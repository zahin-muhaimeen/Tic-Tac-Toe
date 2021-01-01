from random import randint

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def printing_board():
    print("|\t{}\t|\t{}\t|\t{}\t|".format(board[0], board[1], board[2]))
    print("|\t{}\t|\t{}\t|\t{}\t|".format(board[3], board[4], board[5]))
    print("|\t{}\t|\t{}\t|\t{}\t|".format(board[6], board[7], board[8]))

def choosing_player(position):
    if not 0 < position <= 9:
        print("Position not on board")
        return True
    elif board[position - 1] != "-":
        print("Position is occupied by {}".format(board[position - 1]))
        return True
    else:
        board[position - 1] = "X"
        return False


def choosing_computer():
    index = randint(0, 8)
    while board[index] != "-":
        index = randint(0, 8)
    else:
        board[index] = "O"


def checking():
    if board[0] == board[1] == board[2] != "-":
        if board[0] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[3] == board[4] == board[5] != "-":
        if board[3] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[6] == board[7] == board[8] != "-":
        if board[6] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[0] == board[3] == board[6] != "-":
        if board[0] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[1] == board[4] == board[7] != "-":
        if board[3] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[2] == board[5] == board[8] != "-":
        if board[6] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[0] == board[4] == board[8] != "-":
        if board[3] == "X":
            return "X Won!"
        else:
            return "O Won!"
    if board[6] == board[4] == board[2] != "-":
        if board[6] == "X":
            return "X Won!"
        else:
            return "O Won!"
    for i in board:
        if i == "-":
            return None
    return "Draw!"


def main():
    while True:
        printing_board()
        while choosing_player(int(input(": "))):
            pass
        if checking() != None:
            print(checking())
            printing_board()
            return None
        choosing_computer()
        if checking() != None:
            print(checking())
            printing_board()
            return None

main()

