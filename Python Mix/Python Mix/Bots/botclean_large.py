# Head ends here
def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy] == 'd':
        print("CLEAN")
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
    if bstc < posy: 
        print("LEFT")
        return
    if bstr > posx: 
        print("DOWN")
        return
    if bstr < posx: 
        print("UP")
        return
    return                

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
s