import random
import math


# Definition of all functions:
# Printing out the board
def board_print():
    print('\n' + board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])


# Simply explaining the game
def explain_rules():
    print("Welcome!:)\n\nThis is a simple round of tic tac toe. Put in 3 'X's or 'O's in a row and you win!")
    print('\nWhile playing enter a row & column correlated to the field like you see here:')
    print(' | | ')
    print('-+-+-')
    print(' | |X  As you can see here the input for row,column is: 2,3   ')
    print('-+-+-')
    print(' | | ')


# Player can choose which symbol
def choose_symbol():
    global player_Symbol
    global bot_symbol
    while True:
        player_Symbol = input("\nWhich symbol do you want to play? \nEnter 'X' or 'O': ").upper().replace(' ', '')
        if player_Symbol in ['X', 'O']:
            break
        else:
            print('Invalid Input.')

    if player_Symbol == 'O':
        bot_symbol = 'X'
    else:
        bot_symbol = 'O'


# Checks the player input
def turn_player():
    board_print()

    while True:
        player_position = input('\nWhich field do you want to pick?' 
                                '\nWrite the position by typing row,column and hit Enter: ').replace(' ', '').split(",")

        # Checks if inputs are num1, num2 input
        if len(player_position) != 2:
            print('Sorry your input is invalid. Please try again.')
            continue

        if player_position[0] not in ['1', '2', '3'] or player_position[1] not in ['1', '2', '3']:
            print('Sorry your input is invalid. Please try again.')
            continue

        row = int(player_position[0])
        column = int(player_position[1])
        # Check if field is free
        if board[row - 1][column - 1] == ' ':
            board[row - 1][column - 1] = player_Symbol
            break
        else:
            print('Sorry your input is invalid. Please try again.')


# Choosing difficulty Easy vs hard
def choose_bot():

    global turn_bot
    global turn_player_one
    global turn_player_two

    while True:
        choice_bot = input('\nWhich difficulty do you want to pick?'
                           "\nWrite 'e' for easy or 'h' for hard and hit Enter: ").lower().replace(' ', '')
        if choice_bot[0] == 'e':
            turn_bot = easy_bot
            break

        if choice_bot[0] == 'h':
            turn_bot = hard_bot
            break
        print('Sorry your input is invalid. Please try again.')

        # Selecting who starts human or Computer
    turn_player_one = random.choice([turn_player, turn_bot])
    turn_player_two = turn_player if turn_player_one == turn_bot else turn_bot


# Easy bot that moves based on random position generation
def easy_bot():
    while True:
        row, column = random.sample([0, 1, 2], 2)

        if board[row][column] != ' ':
            continue
        else:
            board[row][column] = bot_symbol
            break


# Harder bot with minimax algorithm for deciding best possible move
def hard_bot():
    # Resting current best move and the corresponding value
    best_move = [-1, -1]
    best_value = -math.inf

    # Checking every available field on the board and check their value
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = bot_symbol
                current_value = minimax(9, False, -math.inf, math.inf)
                if current_value > best_value:
                    best_value = current_value
                    best_move = [row, col]
                board[row][col] = ' '

    board[best_move[0]][best_move[1]] = bot_symbol


# Minimax algorithm for evaluating moves on the board for the bot
def minimax(depth, is_maximizing, alpha, beta):
    # Checking win, loos or tie on the deepest level
    # Initial alpha = - infinity and beta = + infinity
    if check_win(player_Symbol, bot_symbol) == -10:
        return (-10-depth)
    if check_win(player_Symbol, bot_symbol) == 10:
        return (10+depth)
    if (check_board_full() == True) or (depth == 0):
        return 0

    # Maximizing player
    if is_maximizing:
        best_value = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = bot_symbol
                    current_value = minimax(depth-1, False, alpha, beta)
                    best_value = max(best_value, current_value)
                    alpha = max(best_value, alpha)
                    board[row][col] = ' '

                    # alpha beta pruning
                if beta <= alpha:
                    break
        return best_value
    # Minimizing player
    else:
        best_value = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player_Symbol
                    current_value = minimax(depth-1, True, alpha, beta)
                    best_value = min(best_value, current_value)
                    beta = min(best_value, beta)
                    board[row][col] = ' '

                    # alpha beta pruning
                if beta <= alpha:
                    break
        return best_value


# Checking if bot or player won
# Bot wins = +10, player wins = -10, no win =0
def check_win(player, bot):

    # Checks for wins in the rows
    for row in range(3):
        if ''.join(board[row]) == (3 * bot):
            return 10
        elif ''.join(board[row]) == (3 * player):
            return -10

    # Checks for the columns
    for col in range(3):
        if ''.join((board[0][col], board[1][col], board[2][col])) == (3 * bot):
            return 10
        elif ''.join((board[0][col], board[1][col], board[2][col])) == (3 * player):
            return -10

    # Checks for the diagonals
    if ''.join((board[0][0], board[1][1], board[2][2])) == (3 * bot):
        return 10
    elif ''.join((board[0][0], board[1][1], board[2][2])) == (3 * player):
        return -10
    if ''.join((board[0][2], board[1][1], board[2][0])) == (3 * bot):
        return 10
    elif ''.join((board[0][2], board[1][1], board[2][0])) == (3 * player):
        return -10


# Asking if they want to play again
def end_game():
    global continue_game
    if input("Do you want to play again? \nEnter 'y' for yes or 'n' for no:").lower() == 'n':
        print('Thanks for playing. :) Goodbye!')
        continue_game = False
    else:
        print("Okay, Let's go!")


# look at the current score and declares winner if needed
def declare_winner(score, full_board):
    global win
    if score == 10:
        board_print()
        print('The winner is the bot!')
        win = True
        end_game()
    if score == -10:
        board_print()
        print('The winner is the player!')
        win = True
        end_game()
    if full_board == True:
        board_print()
        print("It's a tie!")
        end_game()
        win = True


def check_board_full():
    empty_fiels = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False

    return True


# _______________________________________________________________________________________________________
continue_game = True
bot_symbol = ""
player_Symbol = ""

explain_rules()
choose_symbol()

while continue_game == True:
    # Starting board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    # Starting variables

    turn_bot = None
    turn_player_one = None
    turn_player_two = None
    turn_num = 0

    choose_bot()

    if turn_player_one == turn_player:
        print('\nThe Player begins!')
    else:
        print('\nThe bot begins!')

    win = False

    while win == False:

        turn_num += 1
        if turn_num % 2 == 1:
            turn = turn_player_one
        else:
            turn = turn_player_two
        turn()
        declare_winner(check_win(player_Symbol,bot_symbol), check_board_full())

