from random import randint

def next_move(N,board):
    mask_board=[[0 for y1 in range(N)] for x1 in range(N)] 
    for i in range(N):
        for j in range(N):
            if board[i][j]=='h':
                for x in range(N):
                    mask_board[i][x]+=10/float(abs(j-x+0.1))
                    mask_board[x][j]+=10/float(abs(i-x+0.1))
    for i in range(N):
        for j in range(N):
            if board[i][j] in "mhd":
                mask_board[i][j]=-100
    max=0
    mx=0
    my=0
    for i in range(N):
        for j in range(N):
            if mask_board[i][j]>max:
                max=mask_board[i][j]
                mx=i
                my=j
    if max>0:
        print(str(mx)+" "+str(my))
        return
    
    for i in range(N):
        for j in range(N):
            if board[i][j] not in "mdh":
                for dx in [-1,+1]:
                    for dy in [-1,+1]:
                        mask_board[i][j]+=1+rec_calc(i,j,dx,dy,board,N)
    max=1
    count=0
    mx=[]
    my=[]
    for i in range(N):
        for j in range(N):
            if mask_board[i][j]>max:
                max=mask_board[i][j]
                mx=[]
                my=[]
                count=0
            if mask_board[i][j]==max:
                mx.append(i)
                my.append(j)
                count+=1 
                
    if max>1:
        z=randint(0,count-1)
        print(str(mx[z])+" "+str(my[z]))
        return

    k=-1
    while(k<0):
        mx= randint(0,N-1)
        my= randint(0,N-1)
        k=mask_board[mx][my]

    print(str(mx)+" "+str(my))
    return
    
    
                
def rec_calc(x,y,dx,dy, board, N):
    if x+dx in range(N) and y+dy in range(N):
        if board[x+dx][y+dy] not in "md":
            return 1+rec_calc(x+dx,y+dy,dx,dy,board,N)
    return 0
        

if __name__ == "__main__":
    N=int(input())
    board = [[j for j in input().strip()] for i in range(N)]  
    next_move(N,board)