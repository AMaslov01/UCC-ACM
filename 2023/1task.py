N = int(input())
K = int(input())

List = [0] * N

for i in range(0, N):
    List[i] = int(input())

res = 0
cnt = 0
while((cnt + K) < N):
    if List[cnt] == 0:
        cnt += 1
    else:
        for i in range(cnt, cnt + K):
            if List[i] != 0:
                List[i] -= 1
        res += 1


def sum(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum

while sum(List) != 0:
    for i in range(cnt, cnt + K):
        if List[i] != 0:
            List[i] -= 1
    res += 1

print(res)