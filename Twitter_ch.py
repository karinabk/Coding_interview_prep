# Complete the countMatches function below.

#Compare two grids of 1s and 0s


def matrix(grid):
    matrix = []
    for i in grid:
        row = []
        for k in i:
            row.append(k)
        matrix.append(row)
    return matrix


def countMatches(grid1, grid2):
    matrix1 = matrix(grid1)
    matrix2 = matrix(grid2)
    regions1 = findRegion(matrix1)
    regions2 = findRegion(matrix2)
    return len(regions1.intersection(regions2))
    
    
def isSafe(i, j, visited,grid):
    row = len(grid)
    col = len(grid[0])
    return (i >= 0 and i < row and j >= 0 and j < col and not visited[i][j] and grid[i][j])
    
def dfs(row, col, visited,region,grid):
        rowNbr = [ -1,  0, 0,  1];
        colNbr = [  0,  1, -1, 0];
        visited[row][col] = True
        for k in range(4):
            if isSafe(row + rowNbr[k], col + colNbr[k], visited, grid) and grid[row+rowNbr[k]][col+colNbr[k]]=='1':
                region.add((row+rowNbr[k],col+colNbr[k]))
                dfs(row + rowNbr[k], col + colNbr[k], visited, region, grid)
            elif grid[row][col] == '1':
                region.add((row, col))
    
def findRegion(grid):
    if len(grid)==0:
        return []
    row = len(grid)
    col = len(grid[0])
    visited=[[False for j in range(col)]for i in range(row)]
    regions = []
    count = 0
    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and grid[i][j]=='1':
                count+=1
                region=set()
                dfs(i,j,visited,region,grid)
                region = frozenset(region)
                regions.append(region)
    regions=set(regions)
    return regions

    
    
