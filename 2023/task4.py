file_path = 'input.txt'
with open(file_path, 'r') as file:
    N = int(file.readline())
    O = int(file.readline())
    List = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(0, O):
        num = [0] * N
        num = (file.readline())
        data = num.split(" ")
        
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])
        List[x][y] = z



def max_path_down(List, N):
    grid = [[0 for _ in range (N)] for _ in range (N)]
   
    for i in range(1, N):
        grid[0][i] = List[0][i] + grid[0][i - 1]
        grid[i][0] = List[i][0] + grid[i - 1][0]
    for i in range(1, N):
        for j in range(1, N):
            grid[i][j] = List[i][j] + max(grid[i - 1][j], grid[i][j - 1])
    x = N - 1
    y = N - 1
    print(grid)
    while not (x == 0 and y == 0):
        if(grid[x - 1][y] >=  grid[x][y - 1]) and x > 0:
           x -= 1
           List[x][y] = 0
        elif (grid[x][y - 1] >= grid[x - 1][y]) and y > 0:
           y -= 1
           List[x][y] = 0
        elif y == 0:
            x -= 1
            List[x][y] = 0
        elif x == 0:
            y -= 1
            List[x][y] = 0
        print("x: " + str(x))
        print("y: " + str(y))
        print("value: " + str(List[x][y]))
    print(List)
        
            
    return grid[N - 1][N - 1]
    

def max_path_up(List, N):
    
    grid = [[0 for _ in range (N)] for _ in range (N)]
   
    for i in range(N - 2, -1, -1):
        grid[N - 1][i] = List[N - 1][i] + grid[N - 1][i + 1]
        grid[i][N - 1] = List[i][N - 1] + grid[i + 1][N - 1]
    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            grid[i][j] = List[i][j] + max(grid[i + 1][j], grid[i][j + 1])
    return grid[0][0]
print(int(max_path_down(List, N))+ int(max_path_up(List, N)))































