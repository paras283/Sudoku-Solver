def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
        
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    block_row = row - row%3
    block_col = col - col%3
    
    for i in range(3):
        for j in range(3):
            if grid[block_row + i][ block_col + j] == num:
                return False
            
    return True

def solve(grid, row, col):
    
    if col == 9:
        if row == 8:
            return True
        
        row += 1
        col = 0
        
    if grid[row][col] > 0:
        return solve(grid, row, col+1)
    
    for num in range(1,10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            
            if solve(grid, row, col+1):
                return True
            
        grid[row][col] = 0
        
    return False



if __name__ =="__main__":
    
    grid = []
    
    
    flag = 0
    
    while(flag!=1):
        inp = input("Enter:\n")
        print("")
        if len(inp) == 81:
            flag =1
        else:
            print("*******Enter valid Sudoku************")
        
    count = 0
    
    for i in range(9):
        col = []
        for j in range(9):
            col.append(int(inp[count]))
            count += 1
        grid.append(col)
    
        
    
    if solve(grid,0,0):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end = " ")
            print()
        
    else:
        print("No solution")