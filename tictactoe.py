"""
This program is Tic Tac Toe.
This is a single plyer game, and the opponent is Computer.
To win, player or computer must have their marks in,
any row or any column or any diagonal.
"""

import random
import json


def initialise_board(temp_board):
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
    print('''
Welcome to the "Unbeatable Noughts and Crosses" game
The board layout is shown below:''')
    draw_board(board)
    print('When prompted, enter the number of corresponding to the square you want.')

def get_player_move(board):
    print('''
                   00 01 02
                   10 11 12
Choose your square:20 21 22 : ''')
    while True:
        user_choice_row = input('Enter row: ')
        if not user_choice_row.isdigit():
            print('Invalid input. Enter a number.')
            continue
        elif not 0 <= int(user_choice_row) < 3:
            print('Invalid input. Please type a number between (0-2)')
            continue
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
    for m in range(board_length) : # check for main diagonal win
        if board[m][m] != mark:
            win = False
    if win:
        return win
    win = True
    for n in range(board_length): # check for reverse diagonal win
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
    board = initialise_board(board)
    welcome(board)
    while is_match_running:
        while not did_player_input:
            player_row, player_column = get_player_move(board)
            if (player_row, player_column) == (None, None):
                continue
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

def load_scores():
    with open('leaderboard.txt', 'r') as read_file:
        line = read_file.read()
    leaderboard = json.loads(line)
    return leaderboard


def save_score(user_score):
    user_name = input('Enter your name: ')
    leaderboard = load_scores()
    all_players = leaderboard.keys()
    if user_name in  all_players:
        old_score = leaderboard[user_name]
        new_score = old_score + user_score
        leaderboard[user_name] = new_score
    else:
        leaderboard[user_name] = user_score
    with open('leaderboard.txt', 'w') as write_file:
        json.dump(leaderboard, write_file)

def display_leaderboard(users):
    for names, scores in users.items():
        print(names, scores)

def menu():
    score = None
    while True:
        user_choice = input('''
Enter one of the following optins: 
        1 - Play the game
        2 - Save your score in the leaderboard
        3 - Load and display the leaderboard
        q - End the program
1, 2, 3, or q: ''')
        if user_choice.lower() == 'q':
            print('Thanks for playing ')
            break
        elif user_choice == '1':
            score = play_game()
        if score is None and user_choice == '2':
            print('''
Play a game first.''')
        elif user_choice == '2':
            save_score(score)
            score = None
        elif user_choice == '3':
            leaders = load_scores()
            display_leaderboard(leaders)

if __name__ == '__main__':
    menu()
    