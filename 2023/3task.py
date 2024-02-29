N = int(input())
B = int(input())

List = [0] * N
for i in range(0, N):
    List[i] = int(input())
List.sort()

sum = 0
res = 0
i = 0

while True:
    sum += List[i]
    if sum <= B:
        res += 1
    else:
        break
    i += 1
print(res)
