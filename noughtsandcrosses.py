"""This is noughtsandcrosses.py module"""

import random  # for computer random choice
from os.path import exists  # to check if a file exists or not
import json  # to load and store leaderboard
random.seed()  # seed


def draw_board(board):
    """
    This is draw_board function.
    This prints out board in a 3x3 grid with dashes(-) and pipes(|).
    """
    print('-------------')
    for row in board:  # iterates over rows in board
        temp = '| '
        for mark in row:  # iterates over every mark in row
            temp += mark + ' | '
        print(temp)
        print('-------------')


def welcome(board):
    """
    This is the welcome function and prints a blank board.
    """
    print('''
Welcome to the "Unbeatable Noughts and Crosses" game
The board layout is shown below:''')
    draw_board(board)
    print('When prompted, enter the number of corresponding to the square you want.')


def initialise_board(board):
    """
    This is initialize_board function.
    Sets all elements to ' '.
    Returns board.
    """
    for i, row in enumerate(board):  # iterates over rows in board
        for j in range(len(row)):  # iterates over every mark in row
            board[i][j] = ' '
    return board


def get_player_move(board):
    """
    This is get_player_move function.
    Prompts user to input row and column number.
    Checks if user's choice is empty or not.
    Returns row and column.
    """
    print('''
                   00 01 02
                   10 11 12
Choose your square:20 21 22 : ''')
    user_choice_row, user_choice_column = '', ''
    while True:
        user_choice_row = input('Enter row: ')
        if not user_choice_row.isdigit():  # handles non numbers
            print('Invalid input. Enter a number.')
            continue
        if not 0 <= int(user_choice_row) < 3:  # handles all numbers except < 0 and >= 2
            print('Invalid input. Please type a number between (0-2)')
            continue
        while True:
            user_choice_column = input('Enter column: ')
            if not user_choice_column.isdigit():  # handles non numbers
                print('Invalid input. Enter a number.')
                continue
            if not 0 <= int(user_choice_column) < 3:  # handles all numbers except < 0 and >= 2
                print('Invalid input. Please type a number between (0-2)')
            else:
                break
        break
    row = int(user_choice_row)  # conversion to digit
    col = int(user_choice_column)  # conversion to digit
    user_position = board[row][col]
    if not user_position == ' ':  # checks if user's choice is empty or not
        print('Please choose empty space')
        return None, None
    return row, col


def choose_computer_move(board):
    """
    This is choose_computer_move.
    Randomly generate computer's move in a list of all empty spaces.
    Return row and column.
    """
    empty_position = []
    board_length = len(board)
    for i in range(board_length):  # makes a list of all empty position
        for j in range(board_length):
            if board[i][j] == ' ':
                empty_position.append([i, j])
    choice = random.choice(empty_position)  # randomly chooses an empty places
    row = choice[0]
    col = choice[1]
    return row, col


def check_for_win(board, mark):
    """
    This is check_for_win function.
    Checks for rows, columns, main diagonal and reverse diagonal.
    Returns if won or not.
    """
    board_length = len(board)
    for i in range(board_length):  # iterate over rows
        row_win, col_win = True, True  # Check rows and columns
        for j in range(board_length):  # iterate over marks
            if board[i][j] != mark:
                row_win = False
            if board[j][i] != mark:
                col_win = False
        if row_win or col_win:
            return True
    diagonal1_win, diagonal2_win = True, True  # Check diagonals
    for i in range(board_length):  # iterate over rows
        if board[i][i] != mark:
            diagonal1_win = False
        if board[i][board_length - i - 1] != mark:
            diagonal2_win = False
    if diagonal1_win or diagonal2_win:
        return True
    return False


def check_for_draw(board):
    """
    This is check_for_draw function.
    Checks for all mark and if any mark is ' '.
    Returns is_drawn.
    """
    for row in board:  # iterates over rows
        if ' ' in row:  # checks if mark is empty or not
            return False
    return True


def play_game(board):
    """
    This is play_game function.
    Main game is played here.
    Return 1 if player won, -1 if computer won, 0 if game is drawn.
    """
    did_player_input = False
    is_match_running = True
    board = initialise_board(board)  # initializes empty board with ' ' marks
    welcome(board)
    while is_match_running:
        while not did_player_input:
            player_row, player_column = get_player_move(board)  # call get_player_move function
            if (player_row, player_column) == (None, None):  # if player's input is not taken
                continue
            board[player_row][player_column] = 'X'  # replace ' ' by 'X'
            draw_board(board)  # draw current state of board
            break
        if check_for_win(board, 'X'):  # check if user won
            print('Congratulation. You won')
            draw_board(board)  # draw current state of board
            return 1
        if check_for_draw(board):  # check if draw
            draw_board(board)  # draw current state of board
            print('Its a draw')
            return 0
        computer_row, computer_column = choose_computer_move(board)
        board[computer_row][computer_column] = 'O'  # replace ' ' by 'O'
        print('''
Computer's move is''')
        draw_board(board)
        if check_for_win(board, 'O'):  # check if computer won
            print('Sorry you lost')
            draw_board(board)  # draw current state of board
            return -1
        if check_for_draw(board):  # check if draw
            draw_board(board)  # draw current state of board
            print('Its a draw')
            return 0


def menu():
    """
    This is menu function.
    Prompts user to enter 1, 2, 3, q.
    Calls other functions accordingly.
    """
    while True:
        user_choice = input('''
Enter one of the following options: 
    1 - Play the game
    2 - Save your score in the leaderboard
    3 - Load and display the leaderboard
    q - End the program
1, 2, 3, or q: ''')  # prompt user to input 1, 2, 3, q
        if user_choice.lower() in ('1', '2', '3', 'q'):
            return user_choice.lower()
        print('''
    Please print a valid mode''')


def load_scores():
    """
    This is load_scores function.
    Open leaderboard.txt file.
    Use loads function to load dictionary.
    """
    leaderboard = {}
    if not exists('leaderboard.txt'):  # if leaderboard does not exist
        print("\nLeaderboard does not exists.\n")
        with open('leaderboard.txt', 'w', encoding='utf-8') as new_file:
            print('Creating new leaderboard.')
            json.dump({}, new_file)
    with open('leaderboard.txt', 'r', encoding='utf-8') as read_file:
        line = read_file.read()
    try:
        leaderboard = json.loads(line)  # loads all names and score in leaderboard
    except json.JSONDecodeError:  # if leaderboard does not have object
        with open('leaderboard.txt', 'w', encoding='utf-8') as write_file:
            json.dump({}, write_file)
    return leaderboard


def save_score(score):
    """
    This is save_score function.
    Prompt user to input name.
    Calls load_scores function to load all scores.
    Updates dictionary.
    Opens leaderboard.txt on write mode
    Saves using dump function.
    """
    user_name = input('Enter your name: ').strip().lower()  # prompt user to enter name
    leaderboard = load_scores()  # call load_scores function to get dictionary with names and scores
    all_players = leaderboard.keys()  # only get usernames
    if user_name in all_players:  # if user in leaderboard
        old_score = leaderboard[user_name]
        new_score = old_score + score  # update the old score
        leaderboard[user_name] = new_score
    else:  # if user not in leaderboard
        leaderboard[user_name] = score
    with open('leaderboard.txt', 'w', encoding='utf-8') as write_file:
        json.dump(leaderboard, write_file)  # stores all names and scores
        print('\nSaved Successfully.')


def display_leaderboard(leaders):
    """
    This is display_leaderboard function.
    Displays all players and their scores in console.
    """
    print('''
======LEADERBOARD======
''')
    if leaders == {}:  # empty leaderboard
        print('No leaders yet')
    else:
        for names, scores in leaders.items():  # loops through all names and scores
            print(names, 'scored', scores)
