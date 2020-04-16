# Futoshiki Solver

import numpy as np

grid = [
        [0,0,0,0,0],
        [0,0,3,0,0],
        [0,0,0,0,0],
        [2,0,0,0,0],
        [0,0,0,0,3]
                   ]

sign_ud = [
           [0,'U',0,'U',0],
           ['D',0,0,0,0],
           [0,0,0,0,0],
           ['U',0,0,0,0]
                         ]

sign_lr = [
           ['R',0,0,0],
           [0,0,0,0],
           [0,0,'L',0],
           [0,0,0,0],
           [0,'R','L',0]
                         ]
                             

# Function to identify whether number n would fit into entry
def possible(x,y,n):
    # Compare with items in row or column:
    for i in range(len(grid)):
        if grid[x][i] == n:
            return False
        if grid[i][y] == n:
            return False        
        
    # Check for inequality above entry             
    if sign_ud[x-1][y] == 'U': 
        if grid[x-1][y] > n: 
            return False 
    if sign_ud[x-1][y] == 'D':  
        if grid[x-1][y] < n:
            return False    
   
    # Check for inequality to left of entry   
    if sign_lr[x][y-1] == 'L':
        if grid[x][y-1] > n:
            return False 
    if sign_lr[x][y-1] == 'R':
        if grid[x][y-1] < n:
            return False     
    return True
                

def solver(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                for n in range(1,len(grid)+1):
                    if possible(i,j,n) == True:
                        grid[i][j] = n
                        solver(grid)
                        grid[i][j] = 0
                return
    print(np.matrix(grid))  

solver(grid)