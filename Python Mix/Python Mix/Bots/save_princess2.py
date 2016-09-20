#!/bin/python
def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='p':
                pr=i
                pc=j
    if r>pr:
        return "UP"
    if r<pr:
        return "DOWN"
    if c>pc:
        return "LEFT"
    if c<pc:
        return "RIGHT"
    return ""



n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)


"""
//C version
#include <stdio.h>
#include <string.h>
#include <math.h>
void nextMove(int n, int r, int c, char grid[101][101]){
    //logic here
    int i,j;
    int pr,pc;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(grid[i][j]=='p')
            {
                pr=i;
                pc=j;                
            }
        }
    }
    if(r>pr)printf("UP");
    else if(r<pr)printf("DOWN");
    else if(c>pc)printf("LEFT");
    else if(c<pc)printf("RIGHT");
}
int main(void) {

    int n, r, c;

    scanf("%d", &n);
    scanf("%d", &r);
    scanf("%d", &c);

   char grid[101][101];
    
    for(int i=0; i<n; i++) {
        scanf("%s[^\n]%*c", grid[i]);
    }

    nextMove(n, r, c, grid);
    return 0;
}
"""