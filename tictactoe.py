import random

def initialize_board(temp_board):
    temp_board = [  [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
    return temp_board

def draw_board(board):
    print(f"""
 -------------
 | {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -------------
 | {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -------------
 | {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -------------
    """)

def welcome(board):
    print('''Welcome to the "Unbeatable Noughts and Crosses" game
The board layout is shown below:''')
    draw_board(board=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('When prompted, enter the number of corresponding to the square you want.')

def get_player_move(board):
    print('''
                   1 2 3
                   4 5 6
Choose your square:7 8 9 : ''')
    while True:
        user_choice_row = input('Enter row: ')
        if not user_choice_row.isdigit():
            print('Invalid input. Enter a number.')
            continue
        elif not 0 <= int(user_choice_row) < 3:
            print('Invalid input. Please type a number between (0-2)')
        else:
            while True:
                user_choice_column = input('Enter column: ')
                if not user_choice_column.isdigit():
                    print('Invalid input. Enter a number.')
                    continue
                elif not 0 <= int(user_choice_column) < 3:
                    print('Invalid input. Please type a number between (0-2)')
                else:
                    break
        break
    user_row = int(user_choice_row)
    user_column = int(user_choice_column)
    user_position = board[user_row][user_column]
    if not user_position==' ':
        print('Please choose empty space')
        return (None, None)
    return user_row, user_column

def check_for_win(board, mark):
    board_length = len(board)
    for i in range(board_length): # check for row win
        win = True
        for j in range(board_length):
            if board[i][j] != mark:
                win = False
                continue
        if win:
            return win
    for k in range(board_length): # check for column win
        win = True
        for l in range(board_length):
            if board[l][k] != mark:
                win = False
                continue
        if win:
            return win
    win = True
    for m in range(board_length) : # check for main diagonal
        if board[m][m] != mark:
            win = False
    if win:
        return win
    win = True
    for n in range(board_length): # check for reverse diagonal
        o = board_length - n - 1
        if board[n][o] != mark:
            win  = False
    if win:
        return win
    return win

def check_for_draw(board):
    is_drawn = True
    for row in board:
        if ' ' in row:
            is_drawn = False
            return is_drawn
    return is_drawn

def choose_computer_move(board):
    empty_position = []
    board_length = len(board)
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == ' ':
                empty_position.append([i,j])
    choice = random.choice(empty_position)
    return choice[0], choice[1]

def play_game():
    board = []
    did_player_input = False
    is_match_running = True
    board = initialize_board(board)
    welcome(board)
    board = [['O', ' ', ' '], ['O', 'O', ' '], [' ', ' ', ' ']]
    while is_match_running:
        while not did_player_input:
            player_row, player_column = get_player_move(board)
            if (player_row, player_column) == (None, None):
                continue
            else:
                board[player_row][player_column] = 'X'
                draw_board(board)
                break
        if check_for_win(board, 'X'):
            print('Congratulation. You won')
            draw_board(board)
            return 1
        if check_for_draw(board):
            draw_board(board)
            print('Its a draw')
            return 0
        computer_row, computer_column = choose_computer_move(board)
        board[computer_row][computer_column] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            draw_board(board)
            print('Sorry you lost')
            return -1
        if check_for_draw(board):
            draw_board(board)
            print('Its a draw')
            return 0

print(play_game())
