choices=[]
for x in range(0,9):
    choices.append(str(x+1))
PlayerOneTurn=True
winner=False
c=0
def print_board():
    print('\n_______')
    print('|'+choices[0]+'|'+choices[1]+'|'+choices[2]+'|')
    print('-------')
    print('|'+choices[3]+'|'+choices[4]+'|'+choices[5]+'|')
    print('-------')
    print('|'+choices[6]+'|'+choices[7]+'|'+choices[8]+'|')
    print('------\n')

while not winner:
    print_board()

    if PlayerOneTurn:
        print('Player1')
    else:
        print('Player2')

    choice=int(input('>>'))    

    if(choices[choice-1]=='x' or choices[choice-1]=='o'):
        print('illegal entry,Try again')
        continue

    if PlayerOneTurn:
        choices[choice-1]='x'
    else:
        choices[choice-1]='o'

    PlayerOneTurn= not PlayerOneTurn
    c=c+1

    for x in range(0,3):
        y=x*3
        if(choices[y]==choices[y+1]and choices[y]==choices[y+2]):
            winner=True
            print_board()
        if(choices[x]==choices[x+3]and choices[x]==choices[x+6]):
            winner=True
            print_board()
    if((choices[0]==choices[4]and choices[0]==choices[8]) or (choices[2]==choices[4]and choices[0]==choices[6])):
        winner=True
        print_board()

    if c==9:
        for x in range(0,3):
            y=x*3
            if(choices[y]==choices[y+1]and choices[y]==choices[y+2]):
                winner=True
                print_board()
            if(choices[x]==choices[x+3]and choices[x]==choices[x+6]):
                winner=True
                print_board()
        if((choices[0]==choices[4]and choices[0]==choices[8]) or (choices[2]==choices[4]and choices[0]==choices[6])):
            winner=True
            print_board()
        break


if c==9:
    print('Game is Draw And Over')
else:
    print('Player'+str(int(PlayerOneTurn+1))+"win!\n")
    

            




    
