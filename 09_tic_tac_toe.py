import random
import time

def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    

def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input("Do you want to be X or O? ").upper()
    if letter == 'X':
        return ['X', 'O']
    if letter == 'O':
        return ['O','X']

def who_goes_first():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le))

def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def is_space_free(board, move):
    return board[move] == ' '

def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input("What is your next move? ")
    return int(move)

def choose_random_move(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    for i in range(1, 10):
        board_copy = get_board_copy(the_board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i 
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
        if is_winner(board_copy, player_letter):
            return i
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    if is_space_free(board, 5):
        return 5
    return choose_random_move(board, [2, 4, 6, 8])

def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

### no more functions, game play starts here
print("Welcome to Tic Tac Toe\n")

while True:
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print("\nThe " + turn + " will go first.")
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)
            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print("Hooray! You have won the game!")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie.")
                    break
                else:
                    turn = 'computer'
        else:
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print("The computer has won")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie")
                    break
                else:
                    turn = 'player'
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith('y'):
        break