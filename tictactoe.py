#!/usr/bin/env python

def pretty_print_board(board):
	# Pretty-prints the board. Elements start at the upper-left corner.
	print('     1   2   3  ')
	print('   -------------')
	print('A  | ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
	print('   |-----------|')
	print('B  | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
	print('   |-----------|')
	print('C  | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
	print('   -------------')

# Dictionary of algebraic to integer correspondence.
algebraic_dictionary = {'a1': 0, 'a2': 1, 'a3': 2, \
						'b1': 3, 'b2': 4, 'b3': 5, \
                        'c1': 6, 'c2': 7, 'c3': 8}

def check_for_win(board):
	# Checks a given board for a win.
	return ((board[0] == board[1] == board[2] in ('X','O')) or \
		    (board[3] == board[4] == board[5] in ('X','O')) or \
			(board[6] == board[7] == board[8] in ('X','O')) or \
			(board[0] == board[3] == board[6] in ('X','O')) or \
			(board[1] == board[4] == board[7] in ('X','O')) or \
			(board[2] == board[5] == board[8] in ('X','O')) or \
			(board[0] == board[4] == board[8] in ('X','O')) or \
			(board[2] == board[4] == board[6] in ('X','O')))

def verify_space_free(board,space):
	# Checks if the space is not taken, so a move here would be legal.
	if board[space] == '-':
		return True
	else:
		return False

def check_for_tie(board):
	# Checks to see if every space is full (tie condition).
	for i in range (0,9):
		if verify_space_free(board,i):
			return False
	return True

def ask_to_play_again():
	answer = raw_input("Play again? (Yes/no) ")
	if (str.lower(answer) in ('y','yes') or answer == ''):
		return True
	elif str.lower(answer) in ('n','no'):
		return False
	else:
		print "Not a valid response."
		if ask_to_play_again():
			return True
		else:
			return False

def print_current_score():
	print "Current score:"
	print "  Wins for X: " + str(results[1])
	print "  Wins for Y: " + str(results[2])
	print "  Ties: " + str(results['ties'])

# Player 1 is X, Player 2 is O
player_symbols = {1: 'X', 2: 'O'}

def turn(board,player):
	# Take a turn.
	pretty_print_board(current_board)
	alg_move = raw_input('Player ' + str(player) + ' [' + player_symbols[player] + ']: ')
	if str.istitle(alg_move):
		alg_move = str.lower(alg_move)
	if alg_move not in algebraic_dictionary:
		print "'" + alg_move + "' is not a valid space."
		turn(current_board,current_player)
	else:
		move = algebraic_dictionary[alg_move]
		if verify_space_free(current_board,move):
			current_board[move] = player_symbols[player]
		elif not verify_space_free(current_board,move):
			print alg_move + " is already taken by " + current_board[move] + "!"
			turn(current_board,current_player)
		else:
			print "I didn't understand that."
			turn(current_board,current_player)

# Set play_again to True for the first round
play_again = True

# Results are stored as (wins for X, wins for O, ties)
results = {1: 0, 2: 0, 'ties': 0}

# Initialize the game
current_board = ['-','-','-','-','-','-','-','-','-']
current_player = 1

# Loop the game
while True:
	turn(current_board,current_player)
	if check_for_win(current_board):
		pretty_print_board(current_board)
		print player_symbols[current_player] + " wins!"
		results[current_player] = results[current_player] + 1
		print_current_score()
		if not ask_to_play_again():
			break
		else:
			current_board = ['-','-','-','-','-','-','-','-','-']
			current_player = 1
	elif check_for_tie(current_board):
		# If all the spaces are taken without a win, it is a tie
		print "Tie game!"
		results['ties'] = results['ties'] +1
		print_current_score()
		if not ask_to_play_again():
			break
		else:
			current_board = ['-','-','-','-','-','-','-','-','-']
			current_player = 1
	else:
		# Switch players for the next turn
		if current_player == 1:
			current_player = 2
		else:
			current_player = 1