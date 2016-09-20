#!/bin/python
def nextMove(x, y, color, grid):
    colors="-"
    values_board=[[0 for y1 in range(y)] for x1 in range(x)]

    x2=0
    y2=0
    cur=0
    globalcount=9999
    for color_tmp in "VIBGYOR":
        count,mask_board=init_mask_board(color_tmp,x,y,grid)
#        print (color_tmp+str(count)+mask_board)
        for i in range(x):
            for j in range(y):
                tttt,mask_board=recursive(i,j,x,y,mask_board)
                #if tttt>1:
                values_board[i][j]=tttt    
    

        max=9999
        x1=0
        y1=0
        for i in range(x):
            for j in range(y):
                if values_board[i][j]<max and values_board[i][j]>1:
                    x1=i    
                    y1=j
                    max=values_board[i][j]
        if count<globalcount and x1+y1!=0:
            x2=x1
            y2=y1
            globalcount=count
    print(str(x2)+" "+str(y2))

        
    

    
def findNextCol(col,x, y, board):
    for i in range(x):
        for j in range(y):
            if board[i][j] not in col:
                return board[i][j]
    return "none"

def init_mask_board(color,x,y,board):
    mask_board=[[0 for y1 in range(y)] for x1 in range(x)] 
    k=0
    for i in range(x):
        for j in range(y):
            if board[i][j]==color:
                mask_board[i][j]=1
                k+=1
    return [k,mask_board]
    
def recursive(posx,posy,maxx,maxy,mask_board):
    if posx not in range(maxx) or posy not in range(maxy):
        return 0, mask_board
    if mask_board[posx][posy]==0:
        return 0, mask_board
    mask_board[posx][posy]=0
    counter=1
    tmp,mask_board=recursive(posx-1,posy,maxx,maxy,mask_board)
    counter+=tmp
    tmp,mask_board=recursive(posx+1,posy,maxx,maxy,mask_board)
    counter+=tmp
    tmp,mask_board=recursive(posx,posy-1,maxx,maxy,mask_board)
    counter+=tmp
    tmp,mask_board=recursive(posx,posy+1,maxx,maxy,mask_board)
    counter+=tmp
    return [counter,mask_board]
    
        


x,y,k = [ int(i) for i in input().strip().split() ] 
grid = [[i for i in str(input().strip())] for _ in range(x)] 
nextMove(x, y, k, grid)
