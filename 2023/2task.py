calendar_features = input()
calendar_features_list = calendar_features.split(" ")
W = int(calendar_features_list[0])
M = int(calendar_features_list[1])
X = int(calendar_features_list[2])
Y = int(calendar_features_list[3])
Z = int(calendar_features_list[4])

months = input()
months_list = months.split(" ")
N = int(input())

dates = [[0, 0, 0] for _ in range(N)]
date = [0, 0, 0]
for i in range (0, N):
    string = input()
    date = string.split(" ")
    dates[i] = date

def days_in_previous_months(months_list, month):
    sum = 0
    for i in range(0, month):
        sum += int(months_list[i])
    return sum

def days_a_year(month_list):
    sum = 0
    for i in range(0, len(month_list)):
        sum += int(months_list[i])
    return sum

def leap_years(year, X, Y, Z):
    res = 0
    for i in range(1, year + 1):
        if i % X == 0:
            res += 1
        if i % Y == 0 and i % Z != 0:
            res += 1
    return res


for date in dates:
    sum1 = days_a_year(months_list) * int(date[0]) + leap_years(int(date[0]), X, Y, Z) + days_in_previous_months(months_list, int(date[1])) + int(date[2])
    print(sum1 % W)

