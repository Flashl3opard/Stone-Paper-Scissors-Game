import random as r

########################################################################

def yash():
    print('______________________________\n')
    print('PRESS 1 TO CHOOSE STONE     |')
    print('PRESS 2 TO CHOOSE PAPER     |')
    print('PRESS 3 TO CHOOSE SCISSORS  |')
    print('PRESS 4 TO SHOW POINTS      |')
    print('PRESS 5 TO QUIT THE GAME    |')
    print('PRESS 6 TO RESTART THE MATCH|')
    print('______________________________')
def result(c,d):
    if c==5:
        print('>>>>>>CONGRATULATIONS.....YOU WON THE MATCH :)<<<<<<<<<<<<<')
        

    elif d==5:
        print('>>>>>>BOT WON THE MATCH :(<<<<<<<<')
        

    else:
        pass

def border():
    print('------------------------------------------------------------------------------')
    print('\n')


border()
print('WELCOME TO STONE PAPER SCISSOR GAME!')
print('\n                                   created by yash sheorey')

print('________________________________________________________________________________')
input('\n\n>>>>>>>>>>>>>>>>>>>>>>>>>  PRESS ENTER TO START  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n________________________________________________________________________________')


border()
c=0
d=0

for i in range(1,1000):
    result(c,d)
    bot = r.randint(1,3)
    yash()
    
    
    try:
        play = int(input('TYPE HERE: '))
        border()
    except Exception as ValueError:
        print('PLEASE CHOSE EITHER 1,2,3,4 OR 5')
        
        
        
    if bot==1 and play==1:
        print('PLAYER: ROCK\nBOT: ROCK')
        print("---IT'S A TIE---")
        border()
    elif bot==2 and play==1:
        print('PLAYER: ROCK\nBOT: PAPER')
        print('---BOT WINS A POINT---')
        d+=1
        border()
    elif bot==3 and play==1:
        print('PLAYER: ROCK\nBOT: SCISSOR')
        print('---PLAYER WINS A POINT---')
        c+=1
        border()
    elif bot==1 and play==2:
        print('PLAYER: PAPER\nBOT: ROCK')
        print('PLAYER WINS A POINT---')
        c+=1
        border()
    elif bot==1 and play==3:
        print('PLAYER: SCISSOR\nBOT: ROCK')
        print('---BOT WINS A POINT---')
        d+=1
        border()    
    elif bot==2 and play==2:
        print('PLAYER: PAPER\nBOT: PAPER')
        print("---IT'S A TIE---")
        border()
    elif bot==2 and play==3:
        print('PLAYER: SCISSOR\nBOT: PAPER')
        print('---PLAYER WINS A POINT---')
        c+=1
        border()       
    elif bot==3 and play==3:
        print('PLAYER: SCISSOR\nBOT: SCISSOR')
        print("---IT'S A TIE---")
        border()
    elif bot==3 and play==2:
        print('PLAYER: PAPER\nBOT: SCISSOR')
        print('---BOT WINS A POINT---')
        d+=1
        border()    
    elif play==4:
        print("PLAYER's POINTS:",c,"\nBOT's POINTS:",d)
        border()
    elif play==5:
        confirm = input('ARE YOU SURE YOU WANNA QUIT?(y/n):')
        if confirm.lower()=='y':
            print('--BOT WON THE MATCH!---')
            border()
            break
        elif confirm.lower()=='n':
            print('okay..continuing the match...')
            border()
            continue
    elif play==6:
        print('MATCH RESTARTED!')
        continue
    
    else:
        try:
            print('INVALIDE INPUT...TRY AGAIN')
        except Exception as ValueError:
            print('PLEASE TYPE SOMETHING')

    if c==5:
        print('>>>>>>CONGRATULATIONS.....YOU WON THE MATCH :)<<<<<<<<<<<<<')
        break

    elif d==5:
        print('>>>>>>BOT WON THE MATCH :(<<<<<<<<')
        break

    
    
    
