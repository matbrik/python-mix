#!/usr/bin/python3
import os
def next_move(posx, posy, board):
    mem_board,lastMove=load_mem("test.txt")
    #print(mem_board)
    #update mem_board
    try:    
        for i in range(5):
            for j in range(5):
                if board[i][j]!='o':               
                    mem_board[i][j]=board[i][j]  
    except (ValueError,IndexError):
        print(i)
        print(j)
        print(board)
        print(mem_board)
        print(load_mem("test.txt"))
        with open('test.txt', 'r') as content_file:
            content = content_file.read()
            print(content)
    #print(mem_board)

    if mem_board[posx][posy]=='d':
        print("CLEAN")
        save_mem("test.txt",mem_board, lastMove)

        #save_mem("test.txt",mem_board)
        return   
       
    #if lastMove=="None":
    #    print(board)
    #    print(mem_board)
    #greedy strategy from the others if there is a d 
    md= 99
    bstr=-1
    bstc=-1
    for i in range(5):
        for j in range(5):
            if mem_board[i][j]== 'd':
                if((abs(posx-i)+abs(posy-j))<md):
                    md= abs(posx-i)+abs(posy-j)
                    bstr=i
                    bstc=j


    if bstr!=-1:
        if bstc > posy: 
            print("RIGHT")
            save_mem("test.txt",mem_board, "RIGHT")

            return
        if bstc < posy: 
            print("LEFT")
            save_mem("test.txt",mem_board, "LEFT")

            return
        if bstr > posx: 
            print("DOWN")
            save_mem("test.txt",mem_board, "DOWN")

            return
        if bstr < posx: 
            print("UP")
            save_mem("test.txt",mem_board, "UP")

            return

#now i have to decide in which direction go
# gain = 1/dist

    gainUp=0
    for i in range(posx):
        for j in range(5):
            if mem_board[i][j]=='o':
                gainUp+=1/float((abs(posx-i)+abs(posy-j)))
    gainDown=0
    for i in range(posx,5):
        for j in range(5):
            if mem_board[i][j]=='o':
                gainDown+=1/float((abs(posx-i)+abs(posy-j)))
    gainLeft=0
    for i in range(5):
        for j in range(posy):
            if mem_board[i][j]=='o':
                gainLeft+=1/float((abs(posx-i)+abs(posy-j)))
    gainRight=0
    for i in range(5):
        for j in range(posy,5):
            if mem_board[i][j]=='o':
                gainRight+=1/float((abs(posx-i)+abs(posy-j)))

     
    if(gainUp==max(gainUp,gainDown,gainLeft,gainRight) and lastMove!="DOWN" and gainUp!=0 and posx!=0 ):
        
        print("UP")
        save_mem("test.txt",mem_board, "UP")
        return

    if(gainDown==max(gainDown,gainLeft,gainRight) and lastMove!="UP" and gainDown!=0 and posx!=4):
        print("DOWN")
        save_mem("test.txt",mem_board, "DOWN")

        return    
    if(gainLeft==max(gainLeft,gainRight) and lastMove!="RIGHT" and gainLeft!=0 and posy!=0 ):
        print("LEFT")
        save_mem("test.txt",mem_board, "LEFT")

        return        
    if(lastMove!="LEFT" and gainRight!=0 and posy!=4):
        print("RIGHT")
        save_mem("test.txt",mem_board, "RIGHT")
        return


    if(gainUp==max(gainUp,gainDown,gainLeft,gainRight) and gainUp!=0 and posx!=0):
        print("UP")
        save_mem("test.txt",mem_board, "UP")

        return
    if(gainDown==max(gainDown,gainLeft,gainRight) and gainDown!=0 and posx!=4):
        print("DOWN")
        save_mem("test.txt",mem_board, "DOWN")

        return    
    if(gainLeft==max(gainLeft,gainRight) and gainLeft!=0 and posy!=0):
        print("LEFT")
        save_mem("test.txt",mem_board, "LEFT")

        return        
    if(gainRight!=0 and posy!=4):
        print("RIGHT")
        save_mem("test.txt",mem_board, "RIGHT")
        return

    return

def load_mem(filename):

    board_t=[['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
    lastMove="None"
    if not os.path.isfile('./test.txt'):
        return [board_t, lastMove]
    with open( filename ) as f:
        # file read can happen here
        # print "file exists"
        lastMove=f.readline()
        lastMove=lastMove.strip()
        board_t = [[j for j in f.readline().strip()] for i in range(5)]  
        return [board_t, lastMove]

    
def save_mem(filename, mem_board, lastMove):

    with open( filename, "w") as f:
        f.write(lastMove+'\n')
    # print "file write happening here"
        for i in mem_board:
            
            line=""
            for j in i:
                line+=j
            #print(line, file=f)           
            f.write(line + '\n')

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)
