#!/bin/python
def displayPathtoPrincess(n,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='m':
                mr=i
                mc=j
            if grid[i][j]=='p':
                pr=i
                pc=j
    i=mr-pr
    while i!=0:
        if i<0:
            print("DOWN")
            i+=1
        if i>0:
            print("UP")
            i-=1
    i=mc-pc
    while i!=0:
        if i<0:
            print("RIGHT")
            i+=1
        if i>0:
            print("LEFT")
            i-=1
    
    
    
#print all the moves here
m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)

"""
//C version

#include <stdio.h>
#include <string.h>
#include <math.h>
void displayPathtoPrincess(int n, char grid[101][101]){
    //logic here
    int mr=0,mc=0,pr=0,pc=0;
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(grid[i][j]=='m'){
                mr=i;
                mc=j;
            }
            if(grid[i][j]=='p'){
                pr=i;
                pc=j;
            }
            
        }
    }
    i=mr-pr;
    while(i!=0){
        if(i<0){printf("DOWN\n");
               i++;
               }
        if(i>0){printf("UP\n");
               i--;
               }
    }
        i=mc-pc;
    while(i!=0){
        if(i<0){printf("RIGHT\n");
               i++;
               }
        if(i>0){printf("LEFT\n");
               i--;
               }
    }
    
    
}
int main(void) {

    int m;
    scanf("%d", &m);
    char grid[101][101]={};
    char line[101];

    for(int i=0; i<m; i++) {
        scanf("%s", line);
        strcpy(grid[i], line);
    }
    displayPathtoPrincess(m,grid);
    return 0;
}

"""