#this is rthe game board 
board ={
    'T1' : ' ',  'T2' : ' ',  'T3' : ' ', 
    'M1' : ' ',  'M2' : ' ',  'M3' : ' ', 
    'B1' : ' ',  'B2' : ' ',  'B3' : ' ' 
}


#initialise first player
player = 1 
# this will count the total number of moves a player can make, a player can only make 9 moves
total_moves = 0
#this will be used to check if a player wins 
end_check = 0

#this will used to check if a player has won the game 
def check():
    #Check the moves of player one
    # then check if the players moves satisfies  the horizontal condition
    if board['T1']  == 'X' and  board['T2']  == 'X' and board['T3']  == 'X':
        print('player one won!')
        return 1
        
    if board['M1']  == 'X' and  board['M2']  == 'X' and board['M3']  == 'X':
        print('player one won!')
        return 1
        
    if board['B1']  == 'X' and  board['B2']  == 'X' and board['B3']  == 'X':
        print('player one won!')
        return 1
    
    # Then check if the players moves satisfies  the diagonal condition
    if board['T1']  == 'X' and  board['M2']  == 'X' and board['B3']  == 'X':
        print('player one won!')
        return 1
        
    if board['B1']  == 'X' and  board['M2']  == 'X' and board['T3']  == 'X':
        print('player one won!')
        return 1
    
        
    # Then check if the players moves satisfies  the vertical condition
    if board['T1']  == 'X' and  board['M1']  == 'X' and board['B1']  == 'X':
        print('player one won!')
        return 1
        
    if board['T2']  == 'X' and  board['M2']  == 'X' and board['B2']  == 'X':
        print('player one won!')
        return 1
        
    if board['T3']  == 'X' and  board['M3']  == 'X' and board['B3']  == 'X':
        print('player one won!')
        return 1

    #Check the moves of player two
    # then check if the players moves satisfies  the horizontal condition
    if board['T1']  == 'O' and  board['T2']  == 'O' and board['T3']  == 'O':
        print('player two won!')
        return 1
        
    if board['M1']  == 'O' and  board['M2']  == 'O' and board['M3']  == 'O':
        print('player two won!')
        return 1
        
    if board['B1']  == 'O' and  board['B2']  == 'O' and board['B3']  == 'O':
        print('player two won!')
        return 1
    
    # Then check if the players moves satisfies  the diagonal condition
    if board['T1']  == 'O' and  board['M2']  == 'O' and board['B3']  == 'O':
        print('player two won!')
        return 1
        
    if board['B1']  == 'O' and  board['M2']  == 'O' and board['T3']  == 'O':
        print('player two won!')
        return 1
    
        
    # Then check if the players moves satisfies  the vertical condition
    if board['T1']  == 'O' and  board['M1']  == 'O' and board['B1']  == 'O':
        print('player two won!')
        return 1
        
    if board['T2']  == 'O' and  board['M2']  == 'O' and board['B2']  == 'O':
        print('player two won!')
        return 1
        
    if board['T3']  == 'O' and  board['M3']  == 'O' and board['B3']  == 'O':
        print('player two won!')
        return 1

    return 0 


Print('This is the board, if you want to make a move enter the key that is a placeholder of the space you want to make your move ')
print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('B1|B2|B3')
print('***************')

#this loopp will continue to run until the break condition is met 
while True:

    #everytime the loop runs, the updated board is printed 
    print(board['T1'] + '|' + board['T2'] + '|' + board['T3'])
    print('- +- +-')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('- +- +-')
    print(board['B1'] + '|' + board['B2'] + '|' + board['B3'])

    #we will put the value gotten from our check function into end check
    # if 1 is returned from check function we have a winner
     # if 0 is returned from check function the game continues
    end_check = check()

    #this is our break function to check whether the games is over or if we continue playing 
    #this condition checks if the game ends in a  draw , this happens when the total number of moves that can be made has been made and the check funtion still returns 0
    if total_moves == 9 or end_check == 0:
        print('The game is a draw')
        break

    #this is our break function to check whether the games is over or if we continue playing 
    #this condition checks for when the game ends, this happens when the total number of moves that can be made has been made or the check funtion still returns 1
    if total_moves == 9 or end_check == 1:
        if total_moves == 9 or end_check == 0:
            print('The game is a draw')
        break

    #this loop is where the players take thier turns to play 
    while True:
        if player == 1 :
            p1_input = input('player one ')
            if p1_input.upper() in board and  board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                #after the player plays, we switch to the next player
                player = 2
                break
            else:
                print('Invalid input, please try agaain ')
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and  board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                #after the player plays, we switch to the next player
                player = 1 
                break 
            else:
                print('Invalid input, please try agaain ')
                continue
    # we have to increment the total moves varaible after each player plays 
    total_moves += 1
    print('******************************')
    print()

        
    

