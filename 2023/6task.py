
file_path = 'input1.txt'
with open(file_path, 'r') as file:
    N = int(file.readline())
    stones = [0] * N
    for i in range(0, N):
        num = [0] * 3
        num = file.readline()
        data = num.split()
        stones[i] = data
for i in range(0, N):
    stones[i][1] = int(stones[i][1])
    stones[i][2] = int(stones[i][2])
    
def build_grid(stones):
    X = 0
    Y = 0
    listX = [0] * N
    listY = [0] * N
    for i in range(N):
        listX[i] = int(stones[i][1])
        listY[i] = int(stones[i][2])
    if min(listX) < 0:
        for i in range(0, N):
            stones[i][1] += (0 - int(min(listX)))
    if min(listY) < 0:
        for i in range(0, N):
            stones[i][2] += (0 - min(listY))
    for i in range(N):
        listX[i] = int(stones[i][1])
        listY[i] = int(stones[i][2])
    grid = [[0] * (1 + (max(listY) - min(listY))) for _ in range(1 + (max(listX) - min(listX)))]
    for i in range(N):
        x = stones[i][1]
        y = stones[i][2]
        z = stones[i][0] 
        grid[x][y] = z
    return grid
def output_grid(grid):
    n = len(grid)
    for i in range(n):
        print(grid[i])
        
grid = build_grid(stones)
output_grid(grid)





        
    
        


























