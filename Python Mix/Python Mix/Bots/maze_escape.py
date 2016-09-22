"""
#######
#--#--#
#--#--#
e--#--#
#-----#
#######

"""
import os


def next_move(lastMove,board):
    if lastMove==0:
        if board[0][1]=='#' and board[1][2]=='#':     
            print("DOWN")
            return
        if board[0][1]=='-' and board[1][2]=='-':     
            print("UP")
            return
        if board[0][1]=='#' and board[1][2]=='-':     
            print("LEFT")
            return
        if board[0][1]=='-' and board[1][2]=='#':     
            print("RIGHT")
            return


    if lastMove in [1,2,4,5,6,7,8]:
        print("UP") 
        return  
    if lastMove in [3]:
        print("RIGHT")   
        return                 

def init():
    lastMove=0
    filename="test.txt"
    if not os.path.isfile('./test.txt'):
        with open( filename, "w") as f:
            f.write("1")
    else:
        with open( filename ) as f:
        # file read can happen here
        # print "file exists"
            lastMove=f.readline()
            lastMove=int(lastMove.strip())
        with open( filename, "w") as f:
            f.write(str(lastMove+1))
    return lastMove


if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(3)]  

    lastMove=init()
    next_move(lastMove,board)