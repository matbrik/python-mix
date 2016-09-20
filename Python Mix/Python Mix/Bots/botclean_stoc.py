#!/usr/bin/python
def nextMove(posr, posc, board):
    if board[posr][posc]=='d':
        print("CLEAN")
        return
    for i in range(5):
        for j in range(5):
            if board[i][j]=='d':
                r=i
                c=j
    if posr>r:
        print("UP")
        return
    if posr<r:
        print("DOWN")
        return
    if posc>c:
        print("LEFT")
        return
    if posc<c:
        print("RIGHT")
        return
    
    print ""
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)

    
"""
//C version
#include<stdio.h>
#include<string.h>
void nextMove(int posr, int posc, char board[5][5]) {
    int i=0,j=0;
    int r=0, c=0;
    if(board[posr][posc]=='d'){
        printf("CLEAN\n");
        return;
    }
    for(i=0;i<5;i++)
        for(j=0;j<5;j++)
            if(board[i][j]=='d'){r=i;
                                c=j;}
    if((posr-r)>0)printf("UP\n");
    else if((posr-r)<0)printf("DOWN\n");
        else if((posc-c)<0)printf("RIGHT\n");
        else if((posc-c)>0)printf("LEFT\n");
    return;
}
int main(void) {
    int pos[2], i;
    char board[5][5];
    char line[5];
    scanf("%d", &pos[0]);
    scanf("%d", &pos[1]);
    for(i=0; i<5; i++) {
        scanf("%s", line);
        strncpy(board[i], line, 5);
    }
    nextMove(pos[0], pos[1], board);
    return 0;
}
"""