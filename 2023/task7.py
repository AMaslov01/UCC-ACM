str = input()
str = str.upper()
list= []
res = []

for letter in str:
    if not (letter in list):
        list.append(letter)
        res.append(str.count(letter))

print(list[res.index(max(res))], end="")

list.remove(list[res.index(max(res))])
res.remove(max(res))

print(list[res.index(max(res))])
