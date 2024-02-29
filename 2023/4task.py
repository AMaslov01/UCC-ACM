N = int(input())
O = int(input())

List = [[0 for _ in range(N)] for _ in range(N)]

for i in range(0, O):
    num = [0] * N
    num = input()
    data = num.split(" ")
    
    x = int(data[0])
    y = int(data[1])
    z = int(data[2])
    List[x][y] = z

x = 0
y = 0
res = 0
while not (x == N - 1 and y == N - 1):
    x_sum = 0
    y_sum = 0
    for i in range(x, N):
        x_sum += List[x][i]
    print(x_sum)
    for j in range(y, N):
        y_sum += List[j][y]
    print(y_sum)
    if x_sum >= y_sum and y < N - 1:
        y += 1
    if y_sum >= x_sum and x < N - 1:
        x += 1
    print("x: " + str(x))
    print("y: " + str(y))
    res += List[x][y]
    List[x][y] = 0
    

while not (x == 0 and y == 0):
    x_sum = 0
    y_sum = 0
    for i in range(0, x):
        x_sum += List[x][i]
    print(x_sum)
    for j in range(0, y):
        y_sum += List[j][y]
    print(y_sum)
    if x_sum >= y_sum and y > 0:
        y -= 1
    elif y_sum >= x_sum and x > 0:
        x -= 1
    print("x: " + str(x))
    print("y: " + str(y))
    res += List[x][y]
    List[x][y] = 0
    
print(res)
    












