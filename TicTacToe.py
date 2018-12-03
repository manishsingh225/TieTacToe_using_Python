#chess board
import random
import sys
list_board=[" "]*9
def display_board_initial():
	print(list_board[0]+"|"+ list_board[1]+"|"+list_board[2] )
	print("-----")
	print(list_board[3]+"|"+list_board[4]+"|"+list_board[5] )
	print("-----")
	print(list_board[6]+"|"+list_board[7]+"|"+list_board[8] )
	

def display_board(sym,location):
	display_flag = True
	#list_board=[" ","|"," ","|"," "," ","|"," ","|"," "," ","|"," ","|"," "]
	#print(location,location-1)
	if(list_board[location-1]==" "):
		list_board[location-1]=sym.upper()
		print(list_board[0]+"|"+ list_board[1]+"|"+list_board[2] )
		print("-----")
		print(list_board[3]+"|"+list_board[4]+"|"+list_board[5] )
		print("-----")
		print(list_board[6]+"|"+list_board[7]+"|"+list_board[8] )
	else:
		print("Can't change as its was already occupied.")
		display_flag=False
	return display_flag


def Winner(ply_choice):
	return ((list_board[0] == ply_choice and list_board[1] == ply_choice and list_board[2] == ply_choice) or # across the top
			(list_board[3] == ply_choice and list_board[4] == ply_choice and list_board[5] == ply_choice) or # across the middle
			(list_board[6] == ply_choice and list_board[7] == ply_choice and list_board[8] == ply_choice) or # across the bottom
			(list_board[0] == ply_choice and list_board[3] == ply_choice and list_board[6] == ply_choice) or # down the left side
			(list_board[1] == ply_choice and list_board[4] == ply_choice and list_board[7] == ply_choice) or # down the middle
			(list_board[2] == ply_choice and list_board[5] == ply_choice and list_board[8] == ply_choice) or # down the right side
			(list_board[0] == ply_choice and list_board[4] == ply_choice and list_board[8] == ply_choice) or # diagonal
			(list_board[2] == ply_choice and list_board[4] == ply_choice and list_board[6] == ply_choice)) #diagonal
					

def space_checker(i):
	return list_board[i]==" "
			
def full_board_check():
    for i in range(0,9):
        if space_checker(i):
            return False
    return True
def Player_turn():
	if random.randint(0,1)==0:
		return "Player_2"
	return "Player_1"

	
def Play():
	turn=Player_turn()
	print("{0} please select 'X' or ' O':".format(turn))
	ply_choice_1=str(raw_input())
	if ply_choice_1.lower() in ["x","o"]:
		if ply_choice_1.lower() == "x":
			ply_choice_2="O"
		else:
			ply_choice_2="X"
		#print(ply_choice_1,ply_choice_2)
		Player_choice(turn,ply_choice_1,ply_choice_2)
	else:
		print(" Please select from X and o")
		Play()					
					
					
def replay():
	choice=str(raw_input(" Please Enter Y to play again or N to Stop :"))
	if choice.upper() in ["Y","N"]:
		if choice.upper()=="Y":
			list_board=[" "]*9
			return True
		else:
			return False
	else:
		replay()
		
		
def Player_choice(turn,ply_choice_1,ply_choice_2):
	flag = True
	display_board_initial()
	while flag :
		if turn == "Player_1":
			ply_move_1=int(input("Player 1: Please enter the location where you wan to put :"))
			if display_board(ply_choice_1,ply_move_1):
				if Winner(ply_choice_1.upper()):
					print("Player 1 is winner")
					flag = False
				else:
					if full_board_check():
						print("Game is a Tie")
						break
					else:
						turn = "Player_2"
						flag = True
			else:
				ply_move_1=int(input("Player 1: Please enter the location where you wan to put :"))
				if display_board(ply_choice_1,ply_move_1):
					if Winner(ply_choice_1.upper()):
						print("Player 1 is winner")
						flag = False
					else:
						if full_board_check():
							print("Game is a Tie")
							break
						else:
							turn = "Player_2"
							flag = True
				
		else:
			ply_move_2=int(input("Player 2:Please enter the location where you wan to put : "))
			if display_board(ply_choice_2,ply_move_2):
				if Winner(ply_choice_2.upper()):
					print("Player 2 is winner")
					flag = False
				else:
					if full_board_check():
						print("Game is a Tie")
						break
					else:
						turn = "Player_1"
						flag=True
			else:
				ply_move_2=int(input("Player 2:Please enter the location where you wan to put : "))
				if display_board(ply_choice_2,ply_move_2):
					if Winner(ply_choice_2.upper()):
						print("Player 2 is winner")
						flag = False
					else:
						if full_board_check():
							print("Game is a Tie")
							break
						else:
							turn = "Player_1"
							flag=True
	else:
		if replay():
			Play()
		else:
			print("Thanks for playing TicTacToe!!!!")
			sys.exit()
#display_board()
#Player_choice()
Play()
#print(Winner("X"))
