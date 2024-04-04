
board =[["_","_","_"],["_","_","_"],["_","_","_"]]  # 3x3 board

# this function prints the current board when called
def print_board():
    for row in board:
        print(" ".join(row))


# this function queries the user for a row and column number and symbol 
# and calls the make_move function to update the board and calls the check winner and check tie functions after each move.
def play_game():
    player1_symbol = "X"
    player2_symbol = "O"
    player = 1
    while True:
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        if player == 1:
            if make_move(row, col, player1_symbol):
                player = 2
                if check_winner():
                    print_board()
                    print("Player 'X' wins!")
                    play_again()
                    break
                if check_tie():
                    print_board()
                    print("It's a tie!")
                    play_again()
                    break
                print("Player O's turn")
        else:
            if make_move(row, col, player2_symbol):
                player = 1
                if check_winner():
                    print_board()
                    print("Player 'O' wins!")
                    play_again()
                    break
                print("Player X's turn")
        print_board()

# this function takes the row and column number and the player's symbol as input and updates the board, checking to see whether the move is valid, updating the board
# and returning True if the move is valid and False if the move is invalid

def make_move(row, col, player_symbol):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid move. Please enter a valid row and column number.")
        return False
    if board[row][col] == "_":
        board[row][col] = player_symbol
        return True
    else:
        print("Invalid move. Please enter an empty cell.")
        return False


# this function checks the board to see if there is a winner
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "_":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "_":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return True
    return False

# this function checks the board to see if there is a tie
def check_tie():
    for row in board:
        if "_" in row:
            return False
    return True

# this function asks the user if they would like to play 
def play_again():
    while True:
        play_again = input("Would you like to play tic tac toe? Type y/n.")
        if play_again == "y":
            print("Let's start the game!")
            clear_board()
            play_game()
            return True
        else:
            print("Thanks for playing!")
            return False
        
# this function clears the board       
def clear_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = "_"
    print_board()

play_again()