# Tu se ustvari igralno polje za štiri v vrsto.

def create_board():

    board = [[0 for _ in range(7)] for _ in range(6)]
    return board

def print_board(board):

    for row in reversed(board):
        print(row)

board = create_board() # Ustvari igralno polje.
print_board(board) # Ipis igralnega polja.

