# Head ends here
def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy] == 'd':
        print("CLEAN")
        return

    result=TSM(posx,posy,dimx,dimy,board)
    if result != "TOOMANY":
        print (result) 
        return
    md= 99
    bstr=-1
    bstc=-1
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j]== 'd':
                if((abs(posx-i)+abs(posy-j))<md):
                    md= abs(posx-i)+abs(posy-j)
                    bstr=i
                    bstc=j
    if bstc > posy: 
        print("RIGHT")
        return
    
    if bstr > posx: 
        print("DOWN")
        return
    if bstc < posy: 
        print("LEFT")
        return
    if bstr < posx: 
        print("UP")
        return
    return                

def TSM(posx, posy ,dimx, dimy, board):
    count=0
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j]== 'd':
                count+=1
    if count>3:
        return "TOOMANY"
    up=0
    for i in range(posx+1):
        for j in range(dimy):
            if board[i][j]== 'd':
                up+=1
    down=0
    for i in range(posx, dimx):
        for j in range(dimy):
            if board[i][j]== 'd':
                down+=1
    right=0
    for i in range(dimx):
        for j in range(posy,dimy):
            if board[i][j]== 'd':
                right+=1
    left=0
    for i in range(dimx):
        for j in range(posy+1):
            if board[i][j]== 'd':
                left+=1
    if max(up,down, left, right)== up:
        return "UP"
    if max(up,down, left, right)== down:
        return "DOWN"
    if max(up,down, left, right)== left:
        return "LEFT"
    if max(up,down, left, right)== right:
        return "RIGHT"    

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
