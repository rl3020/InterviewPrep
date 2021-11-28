


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    
    ROWS = len(grid)
    COLS = len(grid[0])
    
    # Keep track of all cells visited
    visited_cells = set()
    all_islands = []
    
    # perform dfs from each unvisited cell to find connecting cells 
    def dfs(row, col, visited_cells, curr_island): 
        
        # check if in bounds
        if row < 0 or col < 0 or row == ROWS or col == COLS: 
            return 
        
        # check if already visited cell
        if (row, col) in visited_cells: 
            return
        
        # check if curr cell is water (i.e 0)
        if grid[row][col] == "0": 
            return
        
        visited_cells.add((row, col))
        curr_island.append((row,col))
        
        dfs(row + 1, col, visited_cells, curr_island) #up 
        dfs(row - 1, col, visited_cells, curr_island) #down
        dfs(row, col + 1, visited_cells, curr_island) #right 
        dfs(row, col - 1, visited_cells, curr_island) #left
        
    for r in range(ROWS): 
        for c in range(COLS): 
            if grid[r][c] != "0" and (r,c) not in visited_cells: 
                new_island = []
                dfs(r, c, visited_cells, new_island)
                all_islands.append(new_island)
                
    return len(all_islands)

if __name__ == "__main__": 
    print("result: ", numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

