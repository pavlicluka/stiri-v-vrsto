# Tu se ustvari igralno polje za štiri v vrsto.

def create_board():

    board = [[0 for _ in range(7)] for _ in range(6)]
    return board

def print_board(board):

    for row in reversed(board):
        print(row)

board = create_board() # Ustvari igralno polje.
print_board(board) # Ipis igralnega polja.


def drop_piece(board, column, piece):
    "Dodaj plošček v izbrani stolpec, če je to možno."
    for row in range(5, -1, -1):  
        if board[row][column] == 0:  # Preveri, če je mesto prazno
            board[row][column] = piece  # Postavi plošček
            return True
    return False  

def play_turn(board):
    "Zaprosi uporabnika za izbiro stolpca in izvedi potezo."
    while True:
        try:
            column = int(input("Izberi stolpec (0-6): "))
            if 0 <= column <= 6:  # Preverimo, če je izbira znotraj dovoljenih meja
                if drop_piece(board, column, 1):  
                    break  
                else:
                    print("Stolpec je poln. Prosim izberi drug stolpec.")
            else:
                print("Napačna izbira. Prosim izberi stolpec med 0 in 6.")
        except ValueError:
            print("Prosim vnesi številsko vrednost.")



