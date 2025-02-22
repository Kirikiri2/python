# 9 задача
lst = [1, 44, 7, 9, 3, 2, 1, 44]
indexinput = input("Введите два индекса через запятую: ")
indexarr = list(map(int, indexinput.split(',')))
filt = []
for i in range(len(lst)):
    if i not in indexarr:
        filt.append(lst[i])
print(filt)