"CSE210 Tic-tac-toe - Daniel Christian"

position = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def printBoard():
    print(f"{position[1]} | {position[2]} | {position[3]}")
    print("- + - + - ")
    print(f"{position[4]} | {position[5]} | {position[6]}")
    print("- + - + - ")
    print(f"{position[7]} | {position[8]} | {position[9]}")
    print()

def is_winner(position, player):
	if (position[1] == player and position[2] == player and position[3] == player) or \
		(position[4] == player and position[5] == player and position[6] == player) or \
		(position[7] == player and position[8] == player and position[9] == player) or \
		(position[1] == player and position[4] == player and position[7] == player) or \
		(position[2] == player and position[5] == player and position[8] == player) or \
		(position[3] == player and position[6] == player and position[9] == player) or \
		(position[1] == player and position[5] == player and position[9] == player) or \
		(position[3] == player and position[5] == player and position[7] == player):
		return True
	else:
		return False

def board_full(board):
	if " " in board:
		return False
	else:
		return True

while True:
    printBoard()

    choice = input("X's turn to choose a square (1-9):")
    choice = int(choice)

    if position[choice] == " ":
        position[choice] = "X"
    else:
        print("That place is already filled.\nMove to which place? ")
    
    if is_winner(position, "X"):
        printBoard()
        print ("X wins! Congratulations")
        break
    printBoard()

    if board_full(position):
        print("--- GAME DRAW ---")
        break

    choice = input("O's turn to choose a square (1-9): ")
    choice = int(choice)

    if position[choice] == " ":
        position[choice] = "O"
    else:
        print("That place is already filled. \nMove to which place? ")

    if is_winner(position, "O"):
        printBoard()
        print("O Wins! Congratulations")
        break

    if board_full(position):
        print("--- GAME DRAW ---")

