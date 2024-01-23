# Ustvari igralno polje oz. stolpiče.

def create_board():
    return [[0 for _ in range(7)] for _ in range(6)]

# Izriše igralno polje - 7 stolpcev, začnejo se pri 0. 

def print_board(board):  
    print(" 0 1 2 3 4 5 6") 
    for row in reversed(board):
        print('|' + '|'.join(str(cell) for cell in row) + '|')

def drop_piece(board, column, piece): # Logika za izbiranje stolpca.
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            board[row][column] = piece
            return True
    return False

def check_win(board, piece):

    # Dodaj še funkcijo za preverjanje zmage...

    return False  # Zaenkrat vedno vrne False, manjka logika za preverjanje.

def is_board_full(board):  # Preveri če je polje že polno.
    return all(cell != 0 for row in board for cell in row)

def next_player(current_player):  # Naslednji igralec.
    return 2 if current_player == 1 else 1

def play_turn(board, current_player):
    while True:
        print(f"Na vrsti je igralec {current_player}. Izberi v katero vrsto bi rad vrgel plošček.")
        try:
            column = int(input("Izberi stolpec (0-6): "))
            if 0 <= column <= 6:
                if drop_piece(board, column, current_player):
                    break
                else:
                    print("Stolpec je poln. Prosim izberi drug stolpec.")
            else:
                print("Napačna izbira. Prosim izberi stolpec med 0 in 6.")
        except ValueError:
            print("Prosim vnesi številsko vrednost.")

def play_game():
    board = create_board()
    current_player = 1
    while True:
        print_board(board)
        play_turn(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Zmagal je igralec {current_player}!")
            break
        if is_board_full(board):
            print("Igra je končana z neodločenim izidom!")
            break
        current_player = next_player(current_player)

if __name__ == "__main__":
    play_game()
