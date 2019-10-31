from __future__ import print_function
import random
import sys

print('To play against computer press |1|')
print('To play against player press   |2|')
playMode = input('Choose your option: ')

choices = []

if playMode == "2":
    def printBoard() :
        print( '\n -----')
        print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
        print( ' -----')
        print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
        print( ' -----')
        print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
        print( ' -----\n')
    for x in range (0, 9) :
        choices.append(str(x + 1))

    playerOneTurn = True
    winner = False

    while not winner :
        printBoard()

        if playerOneTurn :
            print( "Player 1:")
        else :
            print( "Player 2:")

        try:
            choice = int(input(">> "))
        except IndexError:
            print("please enter a valid field")
            continue
        if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
            print("illegal move, plase try again")
            continue


        if playerOneTurn :
            choices[choice - 1] = 'X'
        else :
            choices[choice - 1] = 'O'

        playerOneTurn = not playerOneTurn

        for x in range (0, 3) :
            y = x * 3
            if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
                winner = True
                printBoard()
            if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
                winner = True
                printBoard()

        if((choices[0] == choices[4] and choices[0] == choices[8]) or 
           (choices[2] == choices[4] and choices[4] == choices[6])) :
            winner = True
            printBoard()

    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
if playMode == '1':
    board=[i for i in range(0,9)]
    player, computer = '',''


    moves=((1,7,3,9),(5,),(2,4,6,8))

    winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    tab=range(1,10)
    def print_board():
        x=1
        for i in board:
            end = ' | '
            if x%3 == 0:
                 end = ' \n'
                 if i != 1: end+='---------\n'
            char=' '
            if i in ('X','O'): char=i
            x+=1
            print(char,end=end)
            
        
    def select_char():
        chars=('X','O')
        if random.randint(0,1) == 0:
            return chars[::-1]
        return chars

    def can_move(brd, player, move):
        if move in tab and brd[move-1] == move-1:
            return True
        return False

    def can_win(brd, player, move):
        places=[]
        x=0
        for i in brd:
            if i == player: places.append(x)
            x+=1
        win=True
        for tup in winners:
            win=True
            for ix in tup:
                if brd[ix] != player:
                    win=False
                    break
            if win == True:
                break
        return win

    def make_move(brd, player, move, undo=False):
        if can_move(brd, player, move):
            brd[move-1] = player
            win=can_win(brd, player, move)
            if undo:
                brd[move-1] = move-1
            return (True, win)
        return (False, False)


    def computer_move():
        move=-1
    
        for i in range(1,10):
            if make_move(board, computer, i, True)[1]:
                move=i
                break
        if move == -1:
        
            for i in range(1,10):
                if make_move(board, player, i, True)[1]:
                    move=i
                    break
        if move == -1:
        
            for tup in moves:
                for mv in tup:
                    if move == -1 and can_move(board, computer, mv):
                        move=mv
                        break
        return make_move(board, computer, move)

    def space_exist():
        return board.count('X') + board.count('O') != 9

    player, computer = select_char()
    print('Player is [%s] and computer is [%s]' % (player, computer))
    result='%%% Tie ! %%%'
    while space_exist():
        print_board()
        print('# Make your move ! [1-9] : ', end='')
        move = int(input())
        moved, won = make_move(board, player, move)
        if not moved:
            print(' >> Invalid number ! Try again !')
            continue
    
        if won:
            result='*** Congratulations ! You won ! ***'
            break
        elif computer_move()[1]:
            result='=== You lose ! =='
            break

    print_board()
    print(result)



