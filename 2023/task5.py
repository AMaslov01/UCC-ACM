number = int(input())


def isPrime(num):
    flag = False
    if num == 2:
        return True
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        return False
    else:
        return True


def base(num, b):
    res = 0
    x = ""
    while num > 0:
        x += str(num % b)
        num = num // b

    for char in x:
        res += int(char)
    return res


cur_prime = True
for i in range(2, 10):
    if not isPrime((base(number, i))):
        print("NOT")
        cur_prime = False
        break

if cur_prime:
    print("YES")
