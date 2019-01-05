from IPython.display import clear_output
import random


def display_board(board):

    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''
    # Asks player 1 to choose x or o
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    # assign player 2, the opposite marker
    if marker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')


def place_maker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # Win TIC TAC TOE?
    return(
        # ALL ROWS, AND CHECK TO SEE IF THEY ALL SHARE A SAME MARKER
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        # ALL COLUMNS, AND CHECK TO SEE IF THEY ALL SHARE A SAME MARKER
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        # 2 DIAGONALS, CHECK TO SEE IF THEY ALL SHARE A SAME MARKER
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark)
    )


def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
# returns true if board is full
    return True


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1 - 9) '))

    return position


def replay():
    choice = input('Play again? Enter Yes or No')

    return choice == 'Yes'


# while loop to keep running the game
print('Welcome to the game')

while True:
    # Play the game

    # set everything up(board, who's first, choose markers X, O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    # Game play
    while game_on:
        # player one turn
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # place the marker on the position
            place_maker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            else:
                # or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game tie!!')
                    break            # no tie and no win? then next player's turn
                else:
                    turn = 'Player 2'

        else:
               # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # place the marker on the position
            place_maker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                # or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game tie!!')
                    break            # no tie and no win? then next player's turn
                else:
                    turn = 'Player 1'

    if not replay():
        break
    # break out of the while loop on replay()
