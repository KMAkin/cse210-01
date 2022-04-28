# Week 2 assignment tic_tac_toe
# Kris Akin

"""
need to design a board

    1 2 3
    4 5 6
    7 8 9

user input for example 1-9
add selection to board
check for winnner winner chicken dinner (rows, columns, diagonals)
switch between x and o

"""
def main():
    player = current_player('')
    board = create_board()

    while not (is_a_winner(player, board) or is_a_tie(board)):
        print_board(board)
        make_move(player, board)
        player = current_player(player)
    print ("Great Game! Let's play again later...")


def create_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    print ('---------')
    print (f'{board[0]} | {board[1]} | {board[2]}')
    print ('--+---+--')
    print (f'{board[3]} | {board[4]} | {board[5]}')
    print ('--+---+--')
    print (f'{board[6]} | {board[7]} | {board[8]}')
    print ('---------')


def current_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


def make_move(player, board):
    position = int(input(f'Player {player}, choose a position 1-9: '))
    board[position - 1] = player


def is_a_tie(board):
    for position in range(9):
        if board[position] != "x" and board[position] != "o":
            return False
    return True 


def is_a_winner(player, board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
 

if __name__ == "__main__":
    main()