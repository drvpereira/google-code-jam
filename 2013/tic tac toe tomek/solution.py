
board_size = 4;

def read_board():
	return [ input() for _ in range(board_size) ]

def game_status(board):
	result_X = check_player(board, 'X')
	result_O = check_player(board, 'O')
	empty_spaces = check_empty_spaces(board)

	return "X won" if result_X else "O won" if result_O else "Game has not completed" if empty_spaces else "Draw"

def check_player(board, player):
	rows = [ True ] * board_size
	columns = [ True ] * board_size
	diagonals = [ True, True ]

	for i in range(board_size):
		for j in range(board_size):
			rows[i] &= board[i][j] == player or board[i][j] == 'T'
			columns[i] &= board[j][i] == player or board[j][i] == 'T'

		diagonals[0] &= board[i][i] == player or board[i][i] == 'T'
		diagonals[1] &= board[i][board_size - i - 1] == player or board[i][board_size - i - 1] == 'T'

	return sum(rows) > 0 or sum(columns) > 0 or sum(diagonals) > 0

def check_empty_spaces(board):
	return sum([ '.' in board[i] for i in range(board_size) ]) > 0

for i in range(int(input())):
	board = read_board()
	print("Case #{}: {}".format(i+1, game_status(board)))
	input()
