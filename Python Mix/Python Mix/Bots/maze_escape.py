"""
#######
#--#--#
#--#--#
e--#--#
#-----#
#######

"""
def next_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='e':
                if i==0 and j==1:
                        



if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(3)]  
    next_move(board)