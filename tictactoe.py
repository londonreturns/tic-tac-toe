import random

def initialize_board(temp_board):
    temp_board = [  ' ', ' ', ' ',
                    ' ', ' ', ' ',
                    ' ', ' ', ' ']
    return temp_board

def draw_board(board):
    print(f"""
 -------------
 | {board[0]} | {board[1]} | {board[2]} |
 -------------
 | {board[3]} | {board[4]} | {board[5]} |
 -------------
 | {board[6]} | {board[7]} | {board[8]} |
 -------------
    """)
    
def welcome(board):
    print('''Welcome to the "Unbeatable Noughts and Crosses" game
The board layout is shown below:''')
    draw_board(board=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    print('When prompted, enter the number of corresponding to the square you want.')
    
def get_player_move(board):
    while True:
        user_choice = input(
            '''
                        1 2 3
                        4 5 6
Choose your square:     7 8 9 : ''')
        if not user_choice.isdigit():
            print('Please enter a valid cell number')
        elif 0 < int(user_choice) < 10:
            print('ok')
            return int(user_choice)
        else:
            print('invalid number')
            
def choose_computer_move(board):
    empty_position = []
    for i in range(len(board)):
        if board[i] == ' ':
            empty_position.append(i)
    choice = random.choice(empty_position)
    return choice

def main():
    board = []
    board = initialize_board(board)
    welcome(board)
    draw_board(board)
    player_choice = get_player_move(board)
    computer_choice = choose_computer_move(board)
    print(computer_choice)
    ######## need to update board after choice
    ######## need to check users input is in matrix
    ######## only check board after 3 user input
    ######## row columns or 1-9
    
main()