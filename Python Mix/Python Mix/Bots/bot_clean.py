#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    md= 99
    bstr=0
    bstc=0
    for i in range(5):
        for j in range(5):
            if board[i][j]== 'd':
                if((abs(posr-i)+abs(posc-j))<md):
                    md= abs(posr-i)+abs(posc-j)
                    bstr=i
                    bstc=j
    if bstc > posc: 
        print("RIGHT")
        return
    if bstc < posc: 
        print("LEFT")
        return
    if bstr > posr: 
        print("DOWN")
        return
    if bstr < posr: 
        print("UP")
        return
    return      


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)