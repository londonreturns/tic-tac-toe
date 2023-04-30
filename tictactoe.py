"""
This program is Tic Tac Toe.
This is a single plyer game, and the opponent is Computer.
To win, player or computer must have their marks in,
any row or any column or any diagonal.
"""

import random # import random for computer's choice
import json # loads and dumps leaderboard data


def initialise_board(board):
    """
    This is initialize_board function.
    Sets all elements to ' '.
    Returns board.
    """
    board = [   [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']] # sets all marks to space string ' '
    return board

def draw_board(board):
    """
    This is draw_board function.
    This prints out board in a 3x3 grid with dashes(-) and pipes(|).
    """
    print('-------------')
    for row in board: # iterates over rows in board
        temp = '| '
        for mark in row: # iterates over every mark in row
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
    while True:
        user_choice_row = input('Enter row: ')
        if not user_choice_row.isdigit(): # handles non numbers
            print('Invalid input. Enter a number.')
            continue
        if not 0 <= int(user_choice_row) < 3: # handles all numbers except < 0 and >= 2
            print('Invalid input. Please type a number between (0-2)')
            continue
        while True:
            user_choice_column = input('Enter column: ')
            if not user_choice_column.isdigit(): # handles non numbers
                print('Invalid input. Enter a number.')
                continue
            elif not 0 <= int(user_choice_column) < 3: # handles all numbers except < 0 and >= 2
                print('Invalid input. Please type a number between (0-2)')
            else:
                break
        break
    user_row = int(user_choice_row) # conversion to digit
    user_column = int(user_choice_column) # conversion to digit
    user_position = board[user_row][user_column]
    if not user_position==' ': # checks if user's choice is empty or not
        print('Please choose empty space')
        return (None, None)
    return user_row, user_column

def check_for_win(board, mark):
    """
    This is check_for_win function.
    Checks for rows, columns, main diagonal and reverse diagonal.
    Returns if won or not.
    """
    board_length = len(board)
    for i in range(board_length): # check for row win
        did_win = True
        for j in range(board_length):
            if board[i][j] != mark:
                did_win = False
                continue
        if did_win:
            return did_win
    for i in range(board_length): # check for column win
        did_win = True
        for j in range(board_length):
            if board[i][j] != mark:
                did_win = False
                continue
        if did_win:
            return did_win
    did_win = True
    for i in range(board_length) : # check for main diagonal win
        if board[i][i] != mark:
            did_win = False
    if did_win:
        return did_win
    did_win = True
    for i in range(board_length): # check for reverse diagonal win
        j = board_length - i - 1
        if board[i][j] != mark:
            did_win  = False
    if did_win:
        return did_win
    return did_win

def check_for_draw(board):
    """
    This is check_for_draw function.
    Checks for all mark and if any mark is ' '.
    Returns is_drawn.
    """
    is_drawn = True
    for row in board: # iterates over rows
        if ' ' in row: # checks if mark is empty or not
            is_drawn = False
            return is_drawn
    return is_drawn

def choose_computer_move(board):
    """
    This is choose_computer_move.
    Randomly generate computer's move in a list of all empty spaces.
    Return row and column.
    """
    empty_position = []
    board_length = len(board)
    for i in range(board_length): # makes a list of all empty position
        for j in range(board_length):
            if board[i][j] == ' ':
                empty_position.append([i,j])
    choice = random.choice(empty_position) # randomly chooses an empty places
    return choice[0], choice[1]

def play_game():
    """
    This is play_game function.
    Main game is played here.
    Return 1 if player won, -1 if computer won, 0 if draw.
    """
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
        print('''
Computer's move is''')
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
    """
    This is load_scores function.
    Open leaderboard.txt file.
    Use json.loads function to load dictionary.
    """
    with open('leaderboard.txt', 'r', encoding='utf-8') as read_file:
        line = read_file.read()
    leaderboard = json.loads(line)
    return leaderboard


def save_score(user_score):
    """
    This is save_score function.
    Prompt user to input name.
    Calls load_scores function to load all scores.
    Updates dictionary.
    Opens leaderboard.txt on write mode
    Saves using json.dump function.
    """
    user_name = input('Enter your name: ').strip().lower()
    leaderboard = load_scores()
    all_players = leaderboard.keys()
    if user_name in  all_players:
        old_score = leaderboard[user_name]
        new_score = old_score + user_score
        leaderboard[user_name] = new_score
    else:
        leaderboard[user_name] = user_score
    with open('leaderboard.txt', 'w', encoding='utf-8') as write_file:
        json.dump(leaderboard, write_file)

def display_leaderboard(users):
    """
    This is display_leaderboard function.
    Diplays all players and their scores in console.
    """
    for names, scores in users.items():
        print(names, scores)

def menu():
    """
    This is menu function.
    Prompts user to enter 1, 2, 3, q.
    Calls other functions accordingly.
    """
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
    