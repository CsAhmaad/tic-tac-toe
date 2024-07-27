import random
import time
#import numpy as np
class tictac:
    def myinput(tic):
        
        i=random.randint(0,2)
        j=random.randint(0,2)
        if tic[i][j]==0:
            tic[i][j]='X'
            
        else:
            i=random.randint(0,2)
            j=random.randint(0,2)
            if tic[i][j]==0:
                tic[i][j]='X'

    def user(tic):
        i=int(input("Enter place in row: "))
        j=int(input("Enter place in col: "))
        
        if tic[i][j]==0:
            tic[i][j]='Z'
        else:
            print("the place is already used enter again")
            user(tic)


    def print(tic):
        for i in range(0,3):
            print(tic[i])

    def check(board):
    # Check rows
     for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    
    # Check columns
     for i in range(3):
         if board[0][i] == board[1][i] == board[2][i]:
             return board[0][i]
    
    # Check diagonals
     if board[0][0] == board[1][1] == board[2][2]:
         
         return board[0][0]
     elif board[0][2] == board[1][1] == board[2][0]:
         
        return board[0][2]
    
    # No winner
     return None
    #computer entering
    def enter(tic):
        if tic[0][0]=='Z' and tic[0][2]=='Z' and tic[0][1]==0:
            tic[0][1]='X'
        elif tic[0][0]=='Z' and tic[0][1]=='Z' and tic[0][2]==0:
            tic[0][2]='X'
        elif tic[0][1]=='Z' and tic[0][2]=='Z' and tic[0][0]==0:
            tic[0][0]='X'

        elif tic[1][0]=='Z' and tic[1][1]=='Z' and tic[1][2]==0:
            tic[1][2]='X'
        elif tic[1][1]=='Z' and tic[1][2]=='Z' and tic[1][0]==0:
            tic[1][0]='X'
        elif tic[1][0]=='Z' and tic[1][2]=='Z' and tic[1][1]==0:
            tic[1][1]='X'

        elif tic[2][0]=='Z' and tic[2][1]=='Z' and tic[2][2]==0:
            tic[2][2]='X'
        elif tic[2][2]=='Z' and tic[2][2]=='Z' and tic[2][0]==0:
            tic[2][0]='X'
        elif tic[2][0]=='Z' and tic[2][2]=='Z' and tic[2][1]==0:
            tic[2][1]='X'
            
            
        elif tic[0][0]=='Z' and tic[1][0]=='Z' and tic[2][0]==0:
            tic[2][0]='X'
        elif tic[0][0]=='Z' and tic[2][0]=='Z' and tic[1][0]==0:
            tic[1][0]='X'
        elif tic[1][0]=='Z' and tic[2][0]=='Z' and tic[0][0]==0:
            tic[0][0]='X'

         
        elif tic[0][1]=='Z' and tic[1][1]=='Z' and tic[2][1]==0:
            tic[2][1]='X'
        elif tic[0][1]=='Z' and tic[2][1]=='Z' and tic[1][1]==0:
            tic[1][1]='X'
        elif tic[1][1]=='Z' and tic[2][1]=='Z' and tic[0][1]==0:
            tic[0][1]='X'

        elif tic[0][2]=='Z' and tic[1][2]=='Z' and tic[2][2]==0:
            tic[2][2]='X'
        elif tic[0][2]=='Z' and tic[2][2]=='Z' and tic[1][2]==0:
            tic[1][2]='X'
        elif tic[1][2]=='Z' and tic[2][2]=='Z' and tic[0][2]==0:
            tic[0][2]='X'

        elif tic[0][0]=='Z' and tic[1][1]=='Z' and tic[2][2]==0:
            tic[2][2]='X'
        elif tic[0][0]=='Z' and tic[2][2]=='Z' and tic[1][1]==0:
            tic[1][1]='X'
        elif tic[1][1]=='Z' and tic[2][2]=='Z'and tic[0][0]==0 :
            tic[0][0]='X'

        elif tic[0][2]=='Z' and tic[1][1]=='Z' and tic[2][0]==0:
            tic[2][0]='X'
        elif tic[1][1]=='Z' and tic[2][0]=='Z' and tic[0][2]==0:
            tic[0][2]='X'
        elif tic[0][2]=='Z' and tic[2][0]=='Z' and tic[1][1]==0:
            tic[1][1]='X'
            


        elif tic[0][0]=='X' and tic[0][2]=='X' and tic[0][1]==0:
            tic[0][1]='X'
        elif tic[0][0]=='X' and tic[0][1]=='X' and tic[0][2]==0:
            tic[0][2]='X'
        elif tic[0][1]=='X' and tic[0][2]=='X' and tic[0][0]==0:
            tic[0][0]='X'

        elif tic[1][0]=='X' and tic[1][1]=='X' and tic[1][2]==0:
            tic[1][2]='X'
        elif tic[1][1]=='X' and tic[1][2]=='X' and tic[1][0]==0:
            tic[1][0]='X'
        elif tic[1][0]=='X' and tic[1][2]=='X' and tic[1][1]==0:
            tic[1][1]='X'

        elif tic[2][0]=='X' and tic[2][1]=='X' and tic[2][2]==0:
            tic[2][2]='X'
        elif tic[2][2]=='X' and tic[2][2]=='X' and tic[2][0]==0:
            tic[2][0]='X'
        elif tic[2][0]=='X' and tic[2][2]=='X' and tic[2][1]==0:
            tic[2][1]='X'
            
            
        elif tic[0][0]=='X' and tic[1][0]=='X' and tic[2][0]==0:
            tic[2][0]='X'
        elif tic[0][0]=='X' and tic[2][0]=='X' and tic[1][0]==0:
            tic[1][0]='X'
        elif tic[1][0]=='X' and tic[2][0]=='X' and tic[0][0]==0:
            tic[0][0]='X'

         
        elif tic[0][1]=='X' and tic[1][1]=='X' and tic[2][1]==0:
            tic[2][1]='X'
        elif tic[0][1]=='X' and tic[2][1]=='X' and tic[1][1]==0:
            tic[1][1]='X'
        elif tic[1][1]=='X' and tic[2][1]=='X' and tic[0][1]==0:
            tic[0][1]='X'

        elif tic[0][2]=='X' and tic[1][2]=='X' and tic[2][2]==0:
            tic[2][2]='X'
        elif tic[0][2]=='X' and tic[2][2]=='X' and tic[1][2]==0:
            tic[1][2]='X'
        elif tic[1][2]=='X' and tic[2][2]=='X' and tic[0][2]==0:
            tic[0][2]='X'

        elif tic[0][0]=='X' and tic[1][1]=='X' and tic[2][2]==0:
            tic[2][2]='X'
        elif tic[0][0]=='X' and tic[2][2]=='X' and tic[1][1]==0:
            tic[1][1]='X'
        elif tic[1][1]=='X' and tic[2][2]=='X'and tic[0][0]==0 :
            tic[0][0]='X'

        elif tic[0][2]=='X' and tic[1][1]=='X' and tic[2][0]==0:
            tic[2][0]='X'
        elif tic[1][1]=='X' and tic[2][0]=='X' and tic[0][2]==0:
            tic[0][2]='X'
        elif tic[0][2]=='X' and tic[2][0]=='X' and tic[1][1]==0:
            tic[1][1]='X'
        else:
            i=random.randint(0,2)
            j=random.randint(0,2)
            if tic[i][j]==0:
                tic[i][j]='X'
            
            
tic=[[0,0,0],
     [0,0,0],
     [0,0,0]]

'''A=np.array([0,0,0],
             [0,0,0],
             [0,0,0])'''

print("the original board\n",tic)
print("lets play TicTacToe\nI will start first X is mine and Z is yours")

ob=tictac
ob.print(tic)
c=0
choice=str(input("easy or hard: "))
if choice=='easy':
    for i in range(0,9):
        ob.user(tic)
        ob.print(tic)
        a=ob.check(tic)
        if a=='Z' or a=='X':
            print("Hurrah!!! Win by ",a)
            break
        print("computer is entering a value.....")
        time.sleep(2)
        ob.myinput(tic)
        ob.print(tic)
        a=ob.check(tic)
        if a=='Z' or a=='X':
            print("Hurrah!!! Win by ",a)
            break
elif choice=='hard':
    for i in range(0,9):
        ob.user(tic)
        ob.print(tic)
        a=ob.check(tic)
        if a=='Z' or a=='X':
            print("Hurrah!!! Win by ",a)
            break
        print("computer is entering a value.....")
        time.sleep(2)
        ob.enter(tic)
        ob.print(tic)
        a=ob.check(tic)
        if a=='Z' or a=='X':
            print("Hurrah!!! Win by ",a)
            break




